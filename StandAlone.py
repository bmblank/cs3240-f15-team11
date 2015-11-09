from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES
import os.path

def encrypt_file(file, passphrase): #expects passphrase to be a string
    passphrase = str.encode(passphrase)
    if(not os.path.isfile(file)):
        # print("bad file for encrypt func")
        return False
    len_pass = len(passphrase)
    if len_pass > 16:
        passphrase = passphrase[0:16]
    if len_pass < 16:
        extra_needed = 16-len_pass
        passphrase = passphrase+b'a'*extra_needed
    aes = AES.new(passphrase, AES.MODE_CFB, 'SIXTEEN_IV_VALUE')
    plainmsg = ""
    with open(file, 'rb') as f:
        plainmsg = f.read()
    new_file = file+'.enc'
    code = aes.encrypt(plainmsg)
    with open(new_file, 'wb') as n:
        n.write(code)
    # print("successful encrption func")
    print("Your newly encrypted file is: " + new_file)
    return True

def decrypt_file(file, passphrase): #expects passphrase to be a string
    passphrase = str.encode(passphrase)
    len_pass = len(passphrase)
    if(file[-4:] != ".enc"):
        print("bad ending for decrypt func")
        return False
    elif(not os.path.isfile(file)):
        print("bad file for decrypt func")
        return False
    if len_pass > 16:
        passphrase = passphrase[0:16]
    if len_pass < 16:
        extra_needed = 16-len_pass
        passphrase = passphrase+(b'a'*extra_needed)
    aes2 = AES.new(passphrase, AES.MODE_CFB, 'SIXTEEN_IV_VALUE')
    encoded = ""
    with open(file, 'rb') as f:
        encoded = f.read()
    decoded = aes2.decrypt(encoded)
    new_file = 'DEC_' + file[:-4]
    with open(new_file, 'wb') as n:
        n.write(decoded)
    print("Your newly decrypted file is: " + new_file)
    # print(decoded)
    # print("successful decrption func")
    return True


encrypt = input("Are you encrypting (Enter 1) or decrypting (Enter 2)? ")
filename = input("What's the file name? ")
passcode = input("What's the passcode? ")

if encrypt == "1":
    print("Encrypting file")
    encrypt_file(filename, passcode)
else:
    decrypt_file(filename, passcode)




# passphrase = b'Sixteen sdfsddddddddddddddsaldkddddddddddddddddddddddddddddddddddddddddddd'
# print(encrypt_file('011.PNG', passphrase))
# print(decrypt_file('011.PNG.enc', passphrase))
