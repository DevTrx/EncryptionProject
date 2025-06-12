# main.py
import key_manager
import vault
import os

def main():
    print("\n🔐 Secure File Vault")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("Choose an option (1–4): ")

    if choice == "1":
        key_manager.generate_key()
        print("✅ Key generated and saved as 'vault.key'")
    elif choice == "2":
        path = input("Enter the full path to the file you want to encrypt: ")
        if os.path.exists(path):
            vault.encrypt_file(path)
            print("✅ File encrypted.")
        else:
            print("❌ File not found.")
    elif choice == "3":
        path = input("Enter the full path to the .encrypted file: ")
        if os.path.exists(path):
            vault.decrypt_file(path)
            print("✅ File decrypted.")
        else:
            print("❌ File not found.")
    elif choice == "4":
        print("Goodbye!")
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
