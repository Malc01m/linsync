# linsync
Minimal Python scripts to sync a directory between a Linux machine and a Linux SSH server

## Requirements
- The SSH server and your client must be configured to use key authentification.
- Your client must have Python installed.
- These scripts were tested on machines using bash.

## Setup
1. Create the directory to be shared in the home of your client user
2. Open 'settings.py' in an editor
3. Change SERVER_ADDRESS to your SSH server's address
4. Change SERVER_USER to your username on the SSH server
5. Change CLIENT_USER to your username on your client
6. Change DIRECTORY_NAME to the name of the shared directory

## Use
Run linsyncup.py to update the server's copy to match the client's copy.
Run linsyncdwn.py to update the client's copy to match the server's copy.
Run in the terminal to view any errors or warnings.

## Backups
If linsyncdwn.py fails to download a copy of the directory from the server,
it will attempt to restore from a backup it made beforehand. If it wasn't
able to make the backup, it would have stopped before removing the client copy. 
The client *should* have a copy at all times by design. However...

## Warning
There's nothing currently stopping you from running the wrong script and 
overwriting the more recent copy with an older one.

Keep your own backups.
