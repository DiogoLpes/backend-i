

class RegisterUser:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self): #os input são mandados para o dicionario
        return {
            "email": self.email,
            "password": self.password
        }


def AddUser(users):
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    new_user = RegisterUser(username, email, password)
    users.append(new_user.to_dict())
    print("Registo feito com sucesso!")


users = []
AddUser(users)
print(users)

while True:
    print("--------Menu-------")
    print("1. Register")
    print("2. Login")
    print("3. Sair") 
    opcao == input("Escolha uma das opcões: ")

    if opcao == "1":
        AddUser(users)
    else:
        break


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

    print("Login feito com sucesso!")


