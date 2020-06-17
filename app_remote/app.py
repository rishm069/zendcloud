import re
import random
import string
import requests
from requests.auth import HTTPBasicAuth
from bottle import route, run, template, request, response, get, post

def randomStringDigits(stringLength):
    # generate a random string of letters and digits for password and foldername
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

@route('/create')
def create():
        # get Zendesk app information
        qs = request.get_cookie('my_app_params')

        # retriving configuration data from Zendesk
        conf_username = request.get_cookie('username')
        conf_password = request.get_cookie('password')
        conf_url = request.get_cookie('url')
        
        # enforsing HTTPS to Nextcloud server (either HTTP/HTTPS are removed and set to HTTPS in requests)
        if conf_url.startswith('http'):
                conf_url = conf_url.replace("http://","")
        if conf_url.startswith('https'):
                conf_url = conf_url.replace("https://","")
        
        try:
                # creating foldername and password 
                folder_name = randomStringDigits(35)
                folder_password = randomStringDigits(15)

                username = conf_username
                password = conf_password
                auth = HTTPBasicAuth(username, password)

                # folder creation
                mkcol_url = 'https://' + conf_url + '/remote.php/dav/files/' + username + '/' + folder_name
                mkcol_req = requests.request('MKCOL', url=mkcol_url, auth=auth)
                stat_code = mkcol_req.status_code

                if stat_code == 201:
                        # setting share configuration
                        payload = {
                                'shareType':'3',
                                'path' : folder_name,
                                'password' : folder_password,
                                'permissions ' : '8',
                                'publicUpload' : 'true',
                                }
                        headers = {'OCS-APIRequest': 'true'}
                        try:
                                # share creation
                                post_req = requests.request('POST', url='https://' + conf_url + '/ocs/v2.php/apps/files_sharing/api/v1/shares', data=payload, auth=auth, headers=headers)
            
                                # share-link retrival 
                                xml_link = re.findall('<url>(.*?)</url>', post_req.text)
                                share_link = ''.join(xml_link)
            
                                return template('main', qs=qs, success_msg=stat_code, folder_password=folder_password, share_link=share_link)
                        except Exception as e:
                                error_msg = "Can't create share: " + str(e)
                                qs = request.get_cookie('my_app_params')
                                return template('main', qs=qs, error_msg=error_msg) 
                else:
                        error_msg = "Can't create folder: response statuscode " + str(stat_code)
                        qs = request.get_cookie('my_app_params')
                        return template('main', qs=qs, error_msg=error_msg)
        except Exception as e:
                qs = request.get_cookie('my_app_params')
                return template('main', qs=qs, error_msg=str(e))

# initial app location
@route('/sidebar')
def send_iframe_html():
        qs = request.query_string
        response.set_cookie('my_app_params', qs)
        return template('main', qs=qs)

run(host='localhost', port=8080, debug=True)