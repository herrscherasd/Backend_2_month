# c = 1 
# q = "QWERTY"
# d = False


# print(type(c))
# print(type(q))
# print(type(d))



class Human:
    head = 1
    brain = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def names(self):
        print(self.name, self.age)

    def __str__(self):
        return f'name is {self.name} \n' \
               f'age is {self.age}'
    def __len__(self):
        return len(self.name)

    def num(self):
        self.age = self.age * 2
        print(self.age)


c = Human
print(c.brain, c.head)
hum = Human('Beka', 19)
hum.names()

print(len(hum))

hum2 = Human('Николай', 20)
print(hum2)
print(len(hum2))

hum.num()
hum2.num()

print(hum)