#Множественное наследование


# class Учитель:
#     def учить(self = 1):
#         print("Я умею учить")
        
        
# class Строитель:
#     def строить(self = 1):
#         print("Я умею строить")

# class Ученик(Учитель, Строитель):...

# c = Ученик
# c.учить()
# c.строить()


# class A:
#     def __init__(self, s) -> None:
#         self.s = s
#     def a(self = 1):
#         print("A")

# class B:
#     def a(self = 1):
#         print("B")

# class C(B,A):
#     def a(self = 1):
#         print("C")

# a = C
# a.a()
# print(c.__mro__)

# class A:
#     def __init__(self, name) -> None:
#         self.name = name

#     def run(self):
#         print("Rin A")

# class B(A):
#     def __init__(self, age) -> None:
#         self.age = age 

#     def run(self):
#         print("Rin B")

# class C(B):...
    

class O: ... 

class A(O): ... 

class B(O): ... 

class C(O): ... 

class D(O): ... 

class E(O): ... 
 

class K1(A, B, C): ... 

class K2(B, D): ... 

class K3(C, D, E): ... 
 
class Z(K1, K2, K3): ...