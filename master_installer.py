import subprocess
import sys
import os

def run_terminal_command():
    """
    Executes the run_command.py script to run the terminal command.
    This should run first since it calls DeployExtensionGitHub.py.
    """
    try:
        # Ensure the script path is correct
        script_path = os.path.join(os.getcwd(), 'run_command.py')
        if not os.path.exists(script_path):
            print(f"Error: {script_path} does not exist.")
            return

        # Execute the Python script (run_command.py) to run the terminal command
        subprocess.run([sys.executable, script_path], check=True)
        print("run_command.py executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing run_command.py: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")

def run_deploy_extension():
    """
    Executes the DeployExtensionGitHub.py script.
    This will be executed after the terminal command, but typically it's handled by the command in run_command.py.
    """
    try:
        # Ensure the script path is correct
        script_path = os.path.join(os.getcwd(), 'DeployExtensionGitHub.py')
        if not os.path.exists(script_path):
            print(f"Error: {script_path} does not exist.")
            return

        # Execute the Python script (DeployExtensionGitHub.py)
        subprocess.run([sys.executable, script_path], check=True)
        print("DeployExtensionGitHub.py executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing DeployExtensionGitHub.py: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")

def main():
    """
    Main function to execute run_command.py followed by DeployExtensionGitHub.py.
    """
    print("Running run_command.py...")
    run_terminal_command()

    print("Running DeployExtensionGitHub.py...")
    run_deploy_extension()

if __name__ == "__main__":
    main()
