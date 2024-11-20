class Bakery:
    def __init__(self, name,taste):
        self.name = name  # Public
        self._sweetlevel = [1,2,3]  # Protected
        self.__taste = taste  # Private 

    def get_taste(self):
        return self.__taste

class Cookie(Bakery):
    def __init__(self):
        super().__init__("Cookie", "crispy")
        self._sweetlevel = input("sweetness level of the cookie: ")
    

class Brownie(Bakery):
    def __init__(self):
        super().__init__("Brownie","sticky")
        self._sweetlevel = input("sweetness level of the brownie: ")
      

class Cake(Bakery):
    def __init__(self):
        super().__init__("Cake","fluffy")
        self._sweetlevel = input(" sweetness level of the cake: ")

class Person:
    def __init__(self, name, can_make):
        self.name = name
        self.can_make =can_make

    def display_jobs(self):
        sn_names = [job.name for job in self.can_make]
        print(f"{self.name} and can make {', '.join(sn_names)}")



cookie = Cookie()
brownie = Brownie()
cake = Cake()
print(cookie.name, cookie._sweetlevel, cookie.get_taste())
print(brownie.name, brownie._sweetlevel, brownie.get_taste())
print(cake.name, cake._sweetlevel, cake.get_taste())

john = Person("John", [brownie])
marry = Person("Marry", [cookie])
paul = Person("Paul", [cake])
nick = Person("Nick", [cookie, brownie])

john.display_jobs()
marry.display_jobs()
paul.display_jobs()
nick.display_jobs()
