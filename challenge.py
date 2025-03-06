class RegisterUser:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


def AddUser(users):
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    new_user = RegisterUser(username, email, password)
    users.append(new_user)

    print("Registo feito com sucesso!")
    print(users)


users = [{"diogo": "diogo@gmail.com"}, {"pedro": "pedro@gmail.com"}]
AddUser(users)


class LoginUser:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


def LoginUser(users):
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")

    check_user = RegisterUser(username, email, password)

    print(" feito com sucesso!")
