#!/usr/bin/python3
from fabric.api import env, run, put
import os

env.hosts = ['34.207.156.46', '100.26.171.253']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distribute an archive to the webservers"""
    if not os.path.exists(archive_path):
        return False

    """upload the archive to the /tmp/ directory of the webserver"""
    try:
        archive_name = archive_path.split("/")[-1]
        folder_name = archive_name.split(".")[0]
        release_dir = f"/data/web_static/releases/{folder_name}"

        """upload archive"""
        put(archive_path, "/tmp/")

        """create the release directory"""
        run(f"mkdir -p {release_dir}")

        """uncompress the archive to the release directory"""
        run(f"tar -xzf /tmp/{archive_name} -C {release_dir}")

        """delete the archive from the webserver"""
        run(f"rm /tmp/{archive_name}")

        """move the contents from the web_static directory
        to the release directory"""
        run(f"mv {release_dir}/web_static/* {release_dir}")

        """delete the redundant web_static directory"""
        run(f"rm -rf {release_dir}/web_static")

        """delete the symbolic link /data/web_static/current"""
        run(f"rm -rf /data/web_static/current")

        """create a new symbolic link to the new version of the code"""
        run(f"ln -s {release_dir} /data/web_static/current")

        print(f"New versin deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed on {env.host}!: {e}")
        return False
