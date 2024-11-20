# SendRemote
A Python script to transfer files or entire folders from a local machine to a remote server using SCP over SSH.

## Requirements

1. Install the necessary Python libraries:
   ```bash
   pip install paramiko scp
   ```

2. Ensure the SSH server is installed and running on the remote machine:
   ```bash
   sudo apt install openssh-server
   sudo systemctl start ssh
   sudo systemctl enable ssh
   ```

## Configuration

Before using the script, open `send.py` and set the following variables:

- `from_address`: Path to the local directory containing files or folders to be sent.
- `to_address`: IP address or hostname of the remote server.
- `username`: SSH username for the remote server.
- `password`: SSH password for the remote server.
- `remote_path`: Path on the remote server where files or folders will be stored.

## How to Use

### 1. Transfer a Single File

Run the script with the file name as an argument:
```bash
python send.py <file_name>
```

**Example:**
```bash
python send.py example.txt
```
This will transfer the file `example.txt` from the `from_address` directory to the `remote_path` on the remote server.

### 2. Transfer a Full Folder

Use the `-f` option followed by the folder name to transfer an entire directory:
```bash
python send.py -f <folder_name>
```

**Example:**
```bash
python send.py -f my_folder
```
This will recursively transfer all contents of `my_folder` from the `from_address` directory to the `remote_path` on the remote server.

## Notes

- Ensure the SSH credentials are correct, and the SSH service is active on the remote machine.
- Verify that the remote path exists or adjust it as needed.
- For folder transfers, all files and subdirectories will be included.

## Troubleshooting

If you encounter issues:
- Verify that the SSH server is running on the remote machine.
- Check the permissions of the `from_address` and `remote_path`.
- Ensure the file or folder name is correct.

## Example Workflow

1. Edit the script variables in `send.py`:
   ```python
   from_address = "C:\Users\YourUsername\Downloads\ignite"
   to_address = "192.168.18.76"
   username = "your_username"
   password = "your_password"
   remote_path = "/home/your_username/Downloads/"
   ```

2. Start the SSH server on the remote machine:
   ```bash
   sudo systemctl start ssh
   ```

3. Transfer a file:
   ```bash
   python send.py example.txt
   ```

4. Transfer a folder:
   ```bash
   python send.py -f my_folder
   ```

## License

This script is open-source and available for use and modification under the MIT License.

---
