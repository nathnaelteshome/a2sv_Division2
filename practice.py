class Person:
    def __init__(self, x):
        self.name = x

    def talk(self):
        print(f"I am {self.name},I can speak amharic and english")

    def draw(self):
        print("draw")


feven = Person("feven")
nate = Person("nati")


print(feven.name)
feven.talk()
