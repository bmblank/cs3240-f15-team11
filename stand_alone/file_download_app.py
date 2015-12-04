import requests
import json

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

    # username = input("Enter username: ")
    # password = input("Enter password: ")
    username = 'admin'
    password = 'password'

    r = requests.get('http://localhost:8000/api/reports/', auth=(username, password))
    reports = json.loads(r.text)
    print(reports)

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


