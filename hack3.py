class students:
    def __init__(self,Steve, Johnny, Penny,):
        self.Steve=Steve
        self.Johnny=Johnny
        self.Penny=Penny
class Steve:
    def steve(self, name, age, nat):
        self.name=name
        self.age=age
        self.nat=nat
        print(f"name:{self.name} , age:{self.age}, major:{self.nat}")
s=Steve()
s.steve("Steven Schultz", 23, "English")
class Johnny:
    def johny(self , name, age, major):
        self.name=name
        self.age=age
        self.major=major
        print(f"name:{self.name} ,age:{self.age} , major:{self.major} ")
d=Johnny()
d.johny("Jonathan Rosenberg", 24, "Biology")
class Penny:
    def penny(self, name, age, major,):
        self.name = name
        self.age = age
        self.major = major
        print(f"name:{self.name} ,age:{self.age} , major:{self.major} ")
c=Penny()
c.penny("Penelope Meramveliotakis", 21, "Physics")