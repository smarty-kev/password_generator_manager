"""

"""


import os


class PasswordManager:
    def __init__(self, login_state="Logged out"):
        self.login_state = login_state

    @staticmethod
    def create_local_account():
        print("Welcome Newcomer!\nPlease create an account below.")
        username = input("Username : "); password = input("Password : ")
        print(f"Your username is |{username}| and your password is |{password}|. Do not forget it.")
        x = open("credentials.txt", "w")
        x.write(username); x.write("\n"); x.write(password)
        x.close()
        return "Successful Account Creation"

    def login(self):
        print("Please login")
        file = open("credentials.txt", "r")
        creds = file.readlines()  # line 1 = username, line 2 = password
        input_username = input("Username : "); input_password = input("Password : ")
        if creds[0].rstrip() == input_username and creds[1].rstrip() == input_password:
            self.login_state = "Logged in"
            print("Successful Login")
            print(f"Welcome back {creds[0]}!")
        else:
            print("Wrong credentials please try again.")


class PasswordWriter:
    def __init__(self):
        pass

    @staticmethod
    def check_pwd_missing():
        return not os.path.exists("my_passwords.txt")
        # return false if file exists, return true if file doesn't exist

    @staticmethod
    def create_pwd_file():
        x = open("my_passwords.txt", "w")
        x.close()

    @staticmethod
    def write_new_password(note, name, password):
        pwd_file = open("my_passwords.txt", "a")
        pwd_file.write(f"\n\nNote: {note}\nUsername/email: {name}\nPassword: {password}")
        pwd_file.close()
        return "Successful Entry"


class PasswordReader:
    def __init__(self):
        pass

    @staticmethod
    def read_password_file():
        pwd_file = open("my_passwords.txt", "r")
        content = pwd_file.read()
        return content


if __name__ == "__main__":

    pwd_manager = PasswordManager()
    pwd_writer = PasswordWriter()
    pwd_reader = PasswordReader()

    if pwd_writer.check_pwd_missing():
        pwd_writer.create_pwd_file()
    if not os.path.exists("credentials.txt"):
        print(pwd_manager.create_local_account())

    while pwd_manager.login_state != "Logged in":
        pwd_manager.login()
    # testing
    # print(pwd_reader.read_password_file())
    # print(pwd_writer.write_new_password("Amazon", "kev", "123"))


