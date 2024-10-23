import os
import shutil
import sys
import zipfile
import ctypes     # For user prompt
import pyperclip  # Handles clipboard functionality
import urllib.request  # To download the zip file
import tempfile  # To handle temporary file storage

# Define the GitHub repository URL (download the latest zip)
github_zip_url = os.getenv('GITHUB_ZIP_URL', "https://github.com/ArbelTal/pyTal/archive/refs/heads/master.zip")

# Define the destination pyRevit extensions folder
user_profile = os.getenv('USERPROFILE')  # Fetch the user's home directory
pyrevit_extensions_folder = os.getenv(
    'PYREVIT_EXTENSIONS_FOLDER', os.path.join(user_profile, "AppData", "Roaming", "pyRevit", "pyRevit", "extensions")
)

# Function to show a message box to the user
def user_prompt(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Deployment Status", 0)

# Function to deploy the extension by downloading and extracting the GitHub repo zip
def deploy_extension():
    try:
        # Check if the target pyRevit extensions folder exists, if not, create it
        if not os.path.exists(pyrevit_extensions_folder):
            os.makedirs(pyrevit_extensions_folder)

        # Define destination path inside the pyRevit extensions folder
        destination_folder = os.path.join(pyrevit_extensions_folder, "pyTal")

        # If the folder already exists, remove it first (optional)
        if os.path.exists(destination_folder):
            shutil.rmtree(destination_folder)

        # Create a temporary directory to download and extract the zip file
        with tempfile.TemporaryDirectory() as temp_dir:
            # Define paths for zip file and extraction folder
            zip_file_path = os.path.join(temp_dir, "pyTal.zip")
            extract_folder_path = os.path.join(temp_dir, "pyTal-master")

            # Download the zip file from GitHub
            urllib.request.urlretrieve(github_zip_url, zip_file_path)

            # Extract the downloaded zip file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            # Move the extracted folder to the pyRevit extensions folder
            shutil.move(extract_folder_path, destination_folder)

            # The zip file and extracted folder will be automatically deleted when the temp_dir is cleaned up

        # Copy the pyRevit extensions folder path to clipboard
        pyperclip.copy(pyrevit_extensions_folder)

        # Show success message and prompt user
        success_message = (
            f"Extension deployed successfully from GitHub to: {destination_folder}\n\n"
            f"The pyRevit extensions folder path has been copied to your clipboard.\n"
            "You can paste it (Ctrl+V) where needed."
        )
        user_prompt(success_message)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        user_prompt(error_message)
        sys.exit(1)

if __name__ == "__main__":
    deploy_extension()
