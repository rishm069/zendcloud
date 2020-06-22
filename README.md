# zendcloud
Simple Zendesk application for sharefolder creation on a Nexctcloud server

# Requirements
bottle 0.12.18

requests 2.23.0

Nextcloud 18.0.3

# Documentation

To start using this app you need to set up a Nextcloud server and deploy the application (app_remote) as Python Bottle framework application (the other option is to deploy the app on Heroku or use Docker container: https://hub.docker.com/r/rishm/zendcloud)

* Nextcloud and remote app server must be secured via SSL (IP can not be specidied)
* Sharefolder is created as publik share with permissions to upload/download/delete any file for anyone who has a password (more details: https://docs.nextcloud.com/server/15/developer_manual/core/ocs-share-api.html#create-a-new-share)
