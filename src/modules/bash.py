import subprocess

def run(bash_command_string):
    subprocess.run(f"$SUDO {bash_command_string}", shell=True)
