import requests
import json
import crypto
import os

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
    print("SecureShare File Download Application")
    print("The current working directory is", os.getcwd())


    # username = input("Enter username: ")
    # password = input("Enter password: ")
    username = 'admin'
    password = 'password'

    # TODO add error checking for incorrect login info
    # TODO add unresponsive server checking


    r = requests.get('http://localhost:8000/api/reports/', auth=(username, password))
    reports = json.loads(r.text)
    print(reports)

    while True:
        print("What do you want to do?")
        print("\tR - list reports")
        print("\tD - decrypt file")
        print("\tE - encrypt file")
        print("\tX - download report")
        choice = input(">>> ")
        if choice == 'R':
            print("List reports")
            # List the reports the user has access to. Include identifier so it (+ attachment(s)) can be downloaded
        elif choice == 'D':
            print("Decrypt file")
            file_to_decrypt = input("Which file do you want to decrypt? ")
            if not os.path.isfile(file_to_decrypt):
                print("File does not exist!")
            passphrase = input("Enter passphrase: ")
            if crypto.decrypt_file(file_to_decrypt, passphrase):
                print("Done!")
            else:
                print("Decryption did not work.")
        elif choice == 'E':
            print("Encrypt file")
            file_to_encrypt = input("Which file do you want to encrypt? ")
            if not os.path.isfile(file_to_encrypt):
                print("File does not exist!")
            passphrase = input("Enter passphrase: ")
            if crypto.encrypt_file(file_to_encrypt, passphrase):
                print("Done!")
            else:
                print("Encryption did not work.")
        elif choice == 'X':
            print("Download report")
        else:
            print("Incorrect input entered.")


    if reports['count'] == 0:
        print("There are no reports.")
    else:
        reports_list = reports['results']
        for report in reports_list:
            print(report)

        for report in reports_list:
            print('Title:', report['title'])
            print('Author:', report['author'])
            print('Short Description:', report['Short_Description'])
            print('URL:', report['url'])
            print()

        url_input = input("Enter an article URL to download:")
