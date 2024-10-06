import subprocess
from datetime import datetime
import sys
import os

def get_resource_path(relative_path):
    """ Get the path to the bundled resource, works when running as an executable """
    try:
        # If the script is running as an executable (bundled with PyInstaller)
        base_path = sys._MEIPASS
    except AttributeError:
        # If running as a script (not bundled)
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def run_terminal_command():
    """
    Executes the terminal command to create an EXE using PyInstaller.
    """
    try:
        # Get the path to DeployExtensionGitHub.py, using resource path helper
        script_path = get_resource_path('DeployExtensionGitHub.py')

        # Get the current date in "yyyyMMdd" format
        date_str = datetime.now().strftime("%Y%m%d")

        # Define the command to run PyInstaller with the date-stamped name
        command = [
            "pyinstaller",
            "--onefile",
            "--name", f"pyTal_{date_str}",  # This names the executable with a date
            script_path
        ]

        # Run the terminal command
        subprocess.run(command, check=True)
        print("PyInstaller command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running PyInstaller: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    run_terminal_command()
