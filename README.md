# Zendcloud
Simple Zendesk application for sharefolder creation on a Nexctcloud server

# Requirements
* bottle 0.12.18
* requests 2.23.0
* Nextcloud 18.0.3

# Installation

To start using this application: 
1. Set up your own Nextcloud server or use an existing one (Note: Nextcloud server must have resolvable, secured via valid SSL certificate Fully Qualified Domain Name (FQDN)).
2. Set up a user account on a Nexctloud server which will be used to create sharefolders (for details, refer to: https://docs.nextcloud.com/server/15/admin_manual/configuration_user/user_configuration.html). 
3. Deploy server-side part of the application as Python Bottle framework application (the other option is to deploy the app on Heroku or use Docker container: https://hub.docker.com/r/rishm/zendcloud) (Note: the server-side must be secured via valid SSL certificate as well). 
4. Install this application to your Zendesk account and specify the following setting during the installation:\n * Nextcloud_Username - The user on your Nextcloud server that will be used to create sharefolder (this user is unified for all support agents)\n * Nextcloud_Password - the password of the abformentioned user\n * NextcloudServer_URL - Fully Qualified Domain Name (FQDN) that resolves to your Nextcloud server\n * TicketApp_URL - Fully Qualified Domain Name (FQDN) that resolves to your server-side application istance 
* Note: the link must include /sidebar, for example: https://zendcloud.herokuapp.com/sidebar)\n For more details please, refer to: https://github.com/rishm069/zendcloud"
  
# Notes

To start using this app you need to set up a Nextcloud server and deploy the application (app_remote) as Python Bottle framework application (the other option is to deploy the app on Heroku or use Docker container: https://hub.docker.com/r/rishm/zendcloud). The reason for separate server-side deployment is MKCOL request for folder creation which is prohibited for local execution by Zendesk. 

* Nextcloud and remote app server must be secured via SSL (IP can not be specidied) otherwise requests will fail. 
* Sharefolder is created as publik share with permissions to upload/download/delete any file for anyone who has a password (more details: https://docs.nextcloud.com/server/15/developer_manual/core/ocs-share-api.html#create-a-new-share).
