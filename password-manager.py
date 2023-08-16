from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

pwd = input("What is the master password? ")
key = load_key() + pwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, passw = data.split("|")
                decrypted_passw = fer.decrypt(passw.encode()).decode()
                print("User", user, " , Password:", decrypted_passw)
            else:
                print("Invalid data format:", data)


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    encrypted_pwd = fer.encrypt(pwd.encode())
    with open('password.txt', 'a') as f:
        f.write(name + "|" + encrypted_pwd.decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Press q to quit: ").lower()

    if mode == "q":
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode ...")
