# key_manager.py
from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("vault.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("vault.key"):
        raise FileNotFoundError("Key file not found. Generate a key first.")
    with open("vault.key", "rb") as key_file:
        return key_file.read()
