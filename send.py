import os
import sys
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

# Configuration variables
from_address = "C:\\Users\\Faheem\\Downloads\\ignite"  # Local directory where files are stored
to_address = "192.168.18.76"   # Remote machine IP or hostname
username = "kali"    # Remote machine username
password = "kali"    # Remote machine password
remote_path = "/home/kali/Downloads/"  # Path on the remote machine to place the file

def scp_file_transfer(file_name):
    try:
        local_file_path = os.path.join(from_address, file_name)

        if not os.path.isfile(local_file_path):
            print(f"Error: File '{file_name}' does not exist at '{from_address}'")
            return

        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        
        ssh.connect(hostname=to_address, username=username, password=password)
        print(f"Connected to remote machine: {to_address}")
        
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(local_file_path, remote_path)
            print(f"File '{file_name}' successfully transferred to '{to_address}:{remote_path}'")
    
    except Exception as e:
        print(f"Error during SCP transfer: {e}")
    finally:
        ssh.close()

def scp_folder_transfer(folder_path):
    try:
        if not os.path.isdir(folder_path):
            print(f"Error: Folder '{folder_path}' does not exist")
            return

        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        
        ssh.connect(hostname=to_address, username=username, password=password)
        print(f"Connected to remote machine: {to_address}")
        
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(folder_path, remote_path, recursive=True)
            print(f"Folder '{folder_path}' successfully transferred to '{to_address}:{remote_path}'")
    
    except Exception as e:
        print(f"Error during SCP folder transfer: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scp_transfer.py <file_name>")
        print("  python scp_transfer.py -f <folder_name>")
        sys.exit(1)

    if sys.argv[1] == "-f":
        if len(sys.argv) != 3:
            print("Usage: python scp_transfer.py -f <folder_name>")
            sys.exit(1)
        folder_name = sys.argv[2]
        full_folder_path = os.path.join(from_address, folder_name)
        scp_folder_transfer(full_folder_path)
    else:
        file_name = sys.argv[1]
        scp_file_transfer(file_name)
