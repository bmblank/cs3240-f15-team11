import requests

# passphrase = b'Sixteen sdfsddddddddddddddsaldkddddddddddddddddddddddddddddddddddddddddddd'
# print(encrypt_file('011.PNG', passphrase))
# print(decrypt_file('011.PNG.enc', passphrase))

# File Download Application (FDA)
# The FDA is a stand-alone application that will be run on networked computer and communicate with the Django web application.
# A user of this program will be able to:
#   Authenticate using the credentials of a valid registered web-app user.
#   See a list of reports. (This does not have to be as sophisticated as for the web-interface.)
#   Choose a report, display it, and allow the user to download the file or files for that report.
#   Decrypt files if they are encrypted.
#   If you want to require a user to encrypt files with the FDA before uploading them with a report, that is acceptable.

if __name__ == '__main__':
    r = requests.get('http://localhost:8000/api/reports/', auth=('admin', 'password'))
    print(r.text)