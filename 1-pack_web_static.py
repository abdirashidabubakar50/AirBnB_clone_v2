#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the archive filename with the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{timestamp}.tgz"

    # Create the .tgz archive
    result = local(f"tar -cvzf {archive_path} web_static", capture=True)

    # Check if the archive was created successfully
    if result.failed:
        return None

    print(f"Packing web_static to {archive_path}")
    print(f"{result.stdout.strip()}")
    return archive_path
