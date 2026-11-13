
class User:
    def __init__(self, name):
        self.name = name


class Admin(User):
    def use_that(self):
        print("Premium features activated")

user1 = User("Siva")
admin1 = Admin("Admin")


admin1.use_that()
