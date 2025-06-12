# vault.py
from cryptography.fernet import Fernet
import key_manager

def encrypt_file(file_path):
    key = key_manager.load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted)

def decrypt_file(file_path):
    key = key_manager.load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted = fernet.decrypt(encrypted_data)

    original_path = file_path.replace(".encrypted", "")
    with open(original_path, "wb") as file:
        file.write(decrypted)
