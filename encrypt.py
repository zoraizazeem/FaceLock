from cryptography.fernet import Fernet
#key = Fernet.generate_key()
#print(key)

file = open('key.key', 'rb')
'''file.write(key)
file.close()'''
key = file.read()
file.close()

with open('yourpasswords.txt.decrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open('yourpasswords.txt.encrypted', 'wb') as f:
    f.write(encrypted)
