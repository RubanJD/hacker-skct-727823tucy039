# student_name: Ruban J
# roll_number: 12345
# project_name: Password Manager with Encryption
# date: 2026-03-29

from cryptography.fernet import Fernet
import json

# load key
def load_key():
    return open("key.key", "rb").read()

# encrypt
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

# decrypt
def decrypt_password(enc_password):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(enc_password.encode()).decode()

# save password
def save_password():
    site = input("Enter site: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    enc_pass = encrypt_password(password)

    data = {}
    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
    except:
        pass

    data[site] = {"username": username, "password": enc_pass}

    with open("passwords.json", "w") as f:
        json.dump(data, f)

    print("Password saved!")

# view password
def view_password():
    site = input("Enter site: ")

    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)

        enc_pass = data[site]["password"]
        print("Password:", decrypt_password(enc_pass))
    except:
        print("No data found!")

# menu
while True:
    print("\n1. Save Password")
    print("2. View Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        save_password()
    elif choice == "2":
        view_password()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
