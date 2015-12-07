import shutil

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
        print("What do you want to do? Or enter nothing to exit.")
        print("\tr - list reports")
        print("\tx - view report")
        print("\td - decrypt file")
        print("\te - encrypt file")
        choice = input(">>> ").strip()

        if choice == 'r':
            print("List reports")
            # List the reports the user has access to. Include identifier so it (+ attachment(s)) can be downloaded
            r = requests.get('http://localhost:8000/api/reports/', auth=(username, password))
            reports = json.loads(r.text)

            if reports['count'] == 0:
                print("There are no reports.")
            else:
                reports_list = reports['results']
                for report in reports_list:
                    print('Title:', report['title'])
                    print('Author:', report['author'])
                    print('Short Description:', report['Short_Description'])
                    print('Attachments: ', report['Attachments'])
                    print('URL:', report['url'])
                    print()

        elif choice == 'd':
            print("Decrypt file")
            file_to_decrypt = input("Which file do you want to decrypt? ").strip()
            if not os.path.isfile(file_to_decrypt):
                print("File does not exist!")
            passphrase = input("Enter passphrase: ")
            if crypto.decrypt_file(file_to_decrypt, passphrase):
                print("Done!")
            else:
                print("Decryption did not work.")

        elif choice == 'e':
            print("Encrypt file")
            file_to_encrypt = input("Which file do you want to encrypt? ").strip()
            if not os.path.isfile(file_to_encrypt):
                print("File does not exist!")
            passphrase = input("Enter passphrase: ")
            if crypto.encrypt_file(file_to_encrypt, passphrase):
                print("Done!")
            else:
                print("Encryption did not work.")

        elif choice == 'x':
            print("View report")
            url_input = input("Enter an article URL to view: ").strip()
            r = requests.get(url_input, auth=(username, password))
            report = json.loads(r.text)
            print('Title:', report['title'])
            print('Author:', report['author'])
            print('Short Description:', report['Short_Description'])
            print('Detailed Description:', report['Detailed_Description'])
            print('Location of Event:', report['Location_of_Event'])
            print('Created:', report['created'])
            print('Group name:', report['group_name'])
            # print('Folder:', report['folder'])
            print('Attachments: ', report['Attachments'])
            print('URL:', report['url'])
            print()

            attachment_choice_input = input("Would you like to download attachments? (y or n) ")
            if attachment_choice_input == 'y':
                # download attachments for this report
                file_url = report['Attachments']
                print("tryna download", file_url)

                r = requests.get(file_url, stream=True)
                if r.status_code == 200:

                    _, file_name = os.path.split(file_url)
                    full_path = os.path.join('downloaded_attachments', file_name)
                    with open(full_path, 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                        print("Wrote attachment to", full_path)

            elif attachment_choice_input == 'n':
                # not downloading attachments for this report
                pass

        elif choice == '':
            exit()

        else:
            print("Incorrect input entered.")
