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
        x = open("credentials.txt", "x+")
        x.write(username); x.write("\n"); x.write(password)
        x.close()
        if os.path.exists("credentials.txt"):
            return "Successful Account Creation"

    def login(self):
        print("Please login")
        file = open("credentials.txt", "r")
        creds = file.readlines()  # line 1 = username, line 2 = password
        input_username = input("Username : "); input_password = input("Password : ")
        if creds[0].rstrip() == input_username and creds[1].rstrip() == input_password:
            self.login_state = "Logged in"
            print("Successful Login")
            print(f"Welcome back {creds[0].rstrip()}!\n=====================\n")
        else:
            print("Wrong credentials please try again.")

    @staticmethod
    def retrieve_new_password_infos():
        note = input("Note (any information i.e. name of the website) : ")
        username = input("Username (or email) : ")
        password = input("Password : ")
        list_info = [note, username, password]
        return list_info

    @staticmethod
    def delete_last_password():
        try:
            pwd_file = open("my_passwords.txt", "r")
            lines = pwd_file.readlines()
            if lines[-1] != "\n":  # if lines is not empty, will return true
                lines = lines[:-4]
                pwd_file.close()
                pwd_file = open("my_passwords.txt", "w")
                pwd_file.writelines(lines)
                pwd_file.close()
                return "Successfully deleted last password"
            else:
                pwd_file = open("my_passwords.txt", "w")
                pwd_file.writelines("My Passwords\n============\n")
                pwd_file.close()
                return "There are no saved passwords."
        except IOError:
            return "Failed to read file."


class PasswordWriter:
    def __init__(self):
        pass

    @staticmethod
    def check_pwd_missing():
        return not os.path.exists("my_passwords.txt")
        # return false if file exists, return true if file doesn't exist

    @staticmethod
    def create_pwd_file():
        x = open("my_passwords.txt", "x+")
        x.write("My Passwords\n============\n")
        x.close()

    @staticmethod
    def write_new_password(note, name, password):
        pwd_file = open("my_passwords.txt", "a")
        pwd_file.write(f"\n____________\nNote: {note}\nUsername/email: {name}\nPassword: {password}")
        pwd_file.close()
        return "Successful Entry"


class PasswordReader:
    def __init__(self):
        pass

    @staticmethod
    def read_password_file():
        try:
            pwd_file = open("my_passwords.txt", "r")
            content = pwd_file.read()
            if content == "My Passwords\n============\n":  # if there is only the title of the file, will return True
                return "\nThere are no saved passwords."
            else:
                return content
        except IOError:
            print("Failed to read file.")


# menus for cml ui
main_menu = "[1] : save new password\n" \
            "[2] : read passwords\n" \
            "[3] : delete last password\n"   \
            "[x] : exit Password Manager"


if __name__ == "__main__":

    pwd_manager = PasswordManager()
    pwd_writer = PasswordWriter()
    pwd_reader = PasswordReader()

    if pwd_writer.check_pwd_missing():
        pwd_writer.create_pwd_file()
    if not os.path.exists("credentials.txt"):
        print(pwd_manager.create_local_account())

    for i in range(5):
        if pwd_manager.login_state != "Logged in":
            pwd_manager.login()

    if pwd_manager.login_state != "Logged in":
        print("You have entered wrong credentials too many times, please restart the program and try again.")
        exit()

    while True:
        print(main_menu)
        main_menu_input = input("Selection : ")
        if main_menu_input == "1":
            infos = pwd_manager.retrieve_new_password_infos()
            pwd_writer.write_new_password(infos[0], infos[1], infos[2])

        if main_menu_input == "2":
            print("\n")
            print(pwd_reader.read_password_file())

        if main_menu_input == "3":
            print("\n")
            print(pwd_manager.delete_last_password())

        if main_menu_input == "x":
            print("Goodbye :)")
            exit()

        print("\n")
