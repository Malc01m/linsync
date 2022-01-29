import subprocess
import sys
import settings

try:

    localbackup = ["cp", 
    "-r", "/home/" + settings.CLIENT_USER + "/" + settings.DIRECTORY_NAME, 
    "/home/" + settings.CLIENT_USER + "/" + settings.DIRECTORY_NAME + "tmp"]

    subprocess.run(args=localbackup, check=True)

except subprocess.CalledProcessError:
    print("ERROR: Couldn't create backup.")
    sys.exit(1)

try:

    localdelete = ["rm", "-rf", 
    "/home/" + settings.CLIENT_USER + "/" + settings.DIRECTORY_NAME]

    subprocess.run(args=localdelete, check=True)

except subprocess.CalledProcessError:
    print("ERROR: Couldn't delete local copy.")
    sys.exit(1)

restore = False;

try:

    scpdownload = ["scp", "-P", "22", 
    "-r", settings.SERVER_USER + "@" + settings.SERVER_ADDRESS + 
    ":/home/" + settings.SERVER_USER + "/" + settings.DIRECTORY_NAME,
     "/home/" + settings.CLIENT_USER]

    subprocess.run(args=scpdownload, check=True)

except subprocess.CalledProcessError:
    print("ERROR: Couldn't download server copy.")
    restore = True;

if (restore):
    try:

        localbackuprestore = ["mv", 
        "/home/" + settings.CLIENT_USER + "/" + settings.DIRECTORY_NAME + "tmp", 
        "/home/" + settings.CLIENT_USER + "/" + settings.DIRECTORY_NAME]

        subprocess.run(args=localbackuprestore, check=True)

    except subprocess.CalledProcessError:
        print("ERROR: Couldn't restore from backup.")
        sys.exit(1)

try:

    localbackupdel = ["rm", "-rf", 
    "/home/" + settings.CLIENT_USER + "/" + settings.DIRECTORY_NAME + "tmp"]

    subprocess.run(args=localbackupdel, check=True)

except subprocess.CalledProcessError:
    print("WARNING: Couldn't remove backup.")
    sys.exit(1)
