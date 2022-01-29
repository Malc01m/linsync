import subprocess
import sys
import settings

try:

    sshdelete = ["ssh", 
    settings.SERVER_USER + "@" + settings.SERVER_ADDRESS, 
    "cd /home/" + settings.SERVER_USER + 
    " && rm -r " + settings.DIRECTORY_NAME + " && exit"]

    subprocess.run(args=sshdelete, check=True)

except subprocess.CalledProcessError:

    print("WARNING: Couldn't delete server copy. Upload anyway? (Y/N)")
    response = sys.stdin.read(1)
    if (response != 'Y'):
        print("Aborted.")
        sys.exit(1)

try:

    scpupload = ["scp", "-P", "22", 
    "-r", "/home/" + settings.CLIENT_USER + "/" + settings.DIRECTORY_NAME, 
    settings.SERVER_USER + "@" + settings.SERVER_ADDRESS 
    + ":/home/" + settings.SERVER_USER]

    subprocess.run(args=scpupload, check=True)

except subprocess.CalledProcessError:

    print("ERROR: Couldn't upload local copy.")
    sys.exit(1)