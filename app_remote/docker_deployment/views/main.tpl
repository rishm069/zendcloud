<head>
  
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" crossorigin="anonymous"></script>

  <script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
  <script>
  var client = ZAFClient.init();
  let zendeskAcsWSurl;
  client.metadata().then(function (metadata) {
    username=metadata.settings.Nextcloud_Username;
    password=metadata.settings.Nextcloud_Password;
    url=metadata.settings.NextcloudServer_URL;
    document.cookie = "username="+username;
    document.cookie = "password="+password;
    document.cookie = "url="+url;
  });
  
  % if defined('success_msg'):
    client.invoke('notify', 'Request sucessful!');
    var folder_password = '{{folder_password}}';
    var share_link = '{{share_link}}';

client.get('ticket.id').then(function(data) {
  var ticketId = data['ticket.id']
  
  client.request({
      url: '/api/v2/tickets/' + ticketId + '.json',
      type: 'PUT',
      contentType: 'application/json',
      data: JSON.stringify({
          "ticket": {
              "status": "open",
              "comment": {
                  "body": "Share folder has been created. Link: " + share_link + " Paasword is: " + folder_password,
                  "public": false
              }
          }
      })
  })
},
function(response) {
  console.log(response);
}
);

% end

% if defined('error_msg'):
  var msg = "{{error_msg}}";
  client.invoke('notify', msg, 'error');
  console.log(msg);
% end

  </script>

</head>
<body>
  
<div class="card bg-light mb-3" style="max-width: 18rem;">
  <div class="card-body">
    <p class="card-text">Click on the button below to create folder: folder's credentials will be saved into internal comment</p>
    <p><small><a target="_blank" href="https://github.com/rishm069/zendcloud">Documentation and bug report</a></small></p>
  </div>
</div>
 
<div class="text-center"> 
<a class="btn btn-outline-primary" type="button" id="btnFetch" href="create?{{qs}}" role="button">Create Nextcloud folder</a>
</div>

<script>
$(document).ready(function() {
    $("#btnFetch").click(function() {
      // disable button
      $(this).prop("disabled", true);
      // add spinner to button
      $(this).html(
        `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...`
      );
    });
});
</script>
</body>
