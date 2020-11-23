from cryptography.fernet import Fernet
#key = Fernet.generate_key()
#print(key)
def decryptpass():

    file = open('key.key', 'rb')
    '''file.write(key)
    file.close()'''
    key = file.read()
    file.close()
    
    with open('yourpasswords.txt.encrypted', 'rb') as f:
        data = f.read()
    
    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)
    
    with open('yourpasswords.txt.decrypted', 'wb') as f:
        f.write(encrypted)
decryptpass()
