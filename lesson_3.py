#Инкапсуляция
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def may(self):
#         print(f'{self.name} may\n'
#             f'age is {self.age}')
        
# cat = Cat("Beka", 4)
# cat.may()

#Public метод без нижних пробелов
# class Person:
#     def __init__(self, name, last_name, age, secret_key) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.secret = secret_key

# per1 = Person("Beka", "D.Y", 19, "sad1")
# print(per1.secret)
# per1.secret = 1234
# print((per1.secret))



class Person:
    def __init__(self, name, last_name, age, __secret_key) -> None:
        self._name = name
        self._last_name = last_name
        self._age = age
        self.__secret = __secret_key
    def keys(self):
        print(self._name)

    def get_age(self, age = 10):
        if age < 1 or age > 130:
            self.age == age
        raise ValueError("Воз")
    
        


    def _s(self):
        print(self._name, self.__secret)
    # def new(self,newpass):
    #     self.newpass = newpass
    #     self.__secret = self.newpass
    #     return f"new: {self.__secret} "
    # def new2(self):
    #     return f"{self.__secret}"

per1 = Person("Beka", "D.Y", 19, "sad1")
# print(per1.new(987))
# print(per1.new2())
per1._name = "ivan"



# class Microwave:
#     def __init__(self, name) -> None:
#         self.name = name 
    
#     def on(self):
#         self.time()
#         print("Start")
    
#     def time(self):
#         print(input("Input time "))

#     def _hid(self):
#         print("Стоп!")
    
#     def open(self):
#         print("при открытии двери выключить микровэйв")
#         self._hid()
    
#     def stop(self):
#         print("Stop")

# c = Microwave("Samsung")
# c.on()
# c.open()
# c._hid()




# class Чайник:
#     def __init__(self, name) -> None:
#         self.name = name
#     def on(self):
#         self._on()
#         self._boil()

#     def _on(self):
#         print('on')
    
#     def _boil(self):
#         print("boiling")
    
#     def _off(self):
#         print("offнули чайник")

# chainik = Чайник("Tefal")
# chainik.on()

