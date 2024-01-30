import os
import requests
import json
import shutil
import zipfile
from packaging import version

VERSION_FILE_PATH = 'Tsetting/version.json'

def get_local_version(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('version')
    except FileNotFoundError:
        return None

def update_local_version(new_version, file_path):
    data = {'version': new_version}
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def get_github_version():
    response = requests.get('https://raw.githubusercontent.com/D4XG/terrorist/main/version.json')

    if response.status_code == 200:
        return response.json().get('version')
    else:
        print(f"\x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] \x1b[38;5;255m| \x1b[38;5;160mFailed to fetch the GitHub version. Status code: \x1b[38;5;255m{response.status_code}")
        return None

def update_repository():
    # Get the latest version from GitHub
    github_version = get_github_version()

    if github_version:
        # Get the current version of the script
        local_version = get_local_version()

        # Check if an update is needed
        if not local_version or version.parse(github_version) > version.parse(local_version):
            print("\x1b[38;5;160m[ \x1b[38;5;255m# \x1b[38;5;160m] \x1b[38;5;160m| \x1b[38;5;255mUpdating script...")

            # Download the zip file of the repository
            download_url = 'https://github.com/D4XG/terrorist/archive/main.zip'
            response = requests.get(download_url)

            if response.status_code == 200:
                # Save the downloaded content to a temporary file
                with open('update_temp.zip', 'wb') as temp_file:
                    temp_file.write(response.content)

                # Extract the contents to a temporary folder
                with zipfile.ZipFile('update_temp.zip', 'r') as zip_ref:
                    zip_ref.extractall('update_temp')

                # Move the contents from the temporary folder to the main folder
                for item in os.listdir('update_temp/terrorist-main'):
                    source = os.path.join('update_temp/terrorist-main', item)
                    destination = os.path.join('.', item)
                    shutil.move(source, destination)

                # Cleanup temporary files and folder
                os.remove('update_temp.zip')
                shutil.rmtree('update_temp')

                # Update the local version file
                update_local_version(github_version)

                print("\x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] \x1b[38;5;160m| \x1b[38;5;255mTerrorist PANEL updated successfully.")
            else:
                print(f"\x1b[38;5;160m[ \x1b[38;5;255m* \x1b[38;5;160m] \x1b[38;5;160m| Failed to download the update. Status code: \x1b[38;5;255m{response.status_code}")
        else:
            print("\x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] \x1b[38;5;160m| \x1b[38;5;255mTerrorist is already up-to-date.")
    else:
        print("\x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] \x1b[38;5;160m| \x1b[38;5;255mFailed to check for updates.")

if __name__ == '__main__':
    update_repository()
