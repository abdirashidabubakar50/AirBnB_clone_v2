#!/usr/bin/env bash
# sets up the webserver for the deployment of  web_static

# install nginx if not already installed
if ! nginx -v &> /dev/null
then
    sudo apt-get update -y
    sudo apt-get instal nginx -y
fi

# create required directories of they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

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
if [ -L /data/web_static/current ]
then
    sudo rm -f /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update the nginx configuration to serve the content
nginx_conf="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" $nginx_conf
then
    sudo sed -i '/server_name_;/a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' $nginx_conf
fi

# Restart nginx to apply the changes
sudo service nginx restart

# ensure the script executes successfully
exit 0