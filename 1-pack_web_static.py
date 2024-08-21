from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create versions directory if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Get the current time and format it
    now = datetime.now()
    date_str = now.strftime("%Y%m%d%H%M%S")

    # Define the archive filename
    archive_path = f'versions/web_static_{date_str}.tgz'

    # Create the .tgz archive
    result = c.local(f'tar -cvzf {archive_path} web_static', hide=True)
    
    # Check if the archive was created successfully
    if result.ok:
        print(f"Packing web_static to {archive_path}")
        return archive_path
    else:
        return None
