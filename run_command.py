import subprocess


def run_terminal_command():
    """
    Executes the terminal command to create an EXE using PyInstaller.
    """
    try:
        # Define the pyinstaller command
        command = ['pyinstaller', '--onefile', '--name', 'pyTal', 'DeployExtensionGitHub.py']

        # Run the terminal command
        subprocess.run(command, check=True)
        print("PyInstaller command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running PyInstaller: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    run_terminal_command()
