#!/usr/bin/env bash
# sets up the webserver for the deployment of  web_static

chmod +x "$0"

# install nginx if not already installed
if ! dpkg -l | grep -qw nginx; then
    sudo apt update > /dev/null 2>&1
    sudo apt install -y nginx > /dev/null 2>&1
fi

# create required directories of they don't already exist
sudo mkdir -p /data/web_static/releases/test/ > /dev/null 2>&1
sudo mkdir -p /data/web_static/shared/ > /dev/null 2>&1

# create a fake html file to test Nginx configuration
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOF
<html>
<head></head>
<body>
Holberton School
</body>
</html>
EOF
# create symbolic link to test the folder
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current > /dev/null 2>&1
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current > /dev/null 2>&1

# give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/ > /dev/null 2>&1

# update the nginx configuration to serve the content
NGINX_CONF="/etc/nginx/sites-available/default"
if [ -f "$NGINX_CONF" ]; then
    sudo sed -i '/location \/ {/,/}/d' $NGINX_CONF > /dev/null 2>&1
    sudo sed -i '/server_name _;/a location /hbnb_static/ {\n    alias /data/web_static/current/;\n    index index.html;\n}' $NGINX_CONF > /dev/null 2>&1
    sudo systemctl restart nginx > /dev/null 2>&1
else
    exit 1
fi

# ensure the script executes successfully
exit 0