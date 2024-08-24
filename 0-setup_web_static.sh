#!/usr/bin/env bash
# sets up the webserver for the deployment of  web_static

# install nginx if not already installed
if ! nginx -v &> /dev/null
then
    sudo apt-get update
    sudo apt-get instal nginx -y
fi

# create required directories of they don't already exist
sudo mkdir -p /data/
sudo mkdir p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
# create a fake html file to test Nginx configuration
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create symbolic link to test the folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update the nginx configuration to serve the content
nginx_conf="/etc/nginx/sites-available/default"
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {alias /data/web_static/current/;}' $nginx_conf


# Restart nginx to apply the changes
sudo service nginx restart

# ensure the script executes successfully
exit 0