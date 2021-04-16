from cryptography.fernet import Fernet

def GENKEY():
    key = Fernet.generate_key()
    with open("main.key", "wb") as key_file:
        key_file.write(key)

def LOADKEY():
    return open("main.key", "rb").read()

def encrypt_message(message):
    key = LOADKEY()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message
def decrypt_message(encrypted_message):
    key = LOADKEY()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())

    return decrypted_message.decode()