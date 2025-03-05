class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


def AddUser(User):
    print(input("Email:" + User.email))
    print(input("Password:" + User.password))
    print("------Bem Vindo------")
    print("Insire o produto que deseja")


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} costs ${self.price:.2f}"

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"


class Stock(Product):

    def __init__(self, name, stock):
        super().__init__(name)

    def Add_to_cart(self, name, stock):
        self.name.append(stock)

    def Remove_to_cart(self, name, stock):
        self.name.remove(stock)



supermarket = [{"pao": 1.00}, {"madeira": 1.15}]

for items in supermarket[0]:
    print(items)

