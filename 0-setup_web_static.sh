#!/usr/bin/env bash
# Sets up the web server for the deployment of web_static

# Install nginx if not already installed
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'

# Create required directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file to test Nginx configuration
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create symbolic link to test the folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
nginx_conf="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" $nginx_conf; then
    sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {alias /data/web_static/current/;}' $nginx_conf
fi

# Restart Nginx to apply the changes
sudo service nginx restart

# Ensure the script executes successfully
exit 0
