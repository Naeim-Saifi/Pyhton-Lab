# class Rec():
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def Area(self):
#         return self.l*self.b

# l=int(input("Enter Length for rectangle 1: "))  
# b=int(input("Enter Breadth for rectangle 1: "))  
# l2=int(input("Enter Length for rectangle 2: "))  
# b2=int(input("Enter Breadth for rectangle 2: ")) 
# obj=Rec(l,b)
# are1=obj.Area() 
# obj2=Rec(l2,b2) 
# are2=obj2.Area()  
# if(are1==are2):
#     print("Same")
# else:
#     print("Not same")  


# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name of Person ",self.name)
#         print("Age of Person ",self.age)
# # obj=Person("Naeim Saifi",22)
# # obj.display()
# class Student(Person):
#     def __init__(self, name, age): 
#         super().__init__(name, age)
# obj=Student("Naeim Saifi",22)
# obj.display()

# class EquiTri():
#     def __init__(self,l1,l2,l3):
#         self.l1=l1
#         self.l2=l2
#         self.l3=l3
#     def equl(self):
#         if(self.l1==self.l2 and self.l2==self.l3):
#             print("Triangle is Equilateral")
#         else:
#             print("Triangle is not Equilateral")
# obj=EquiTri(3,36,3)
# obj.equl()

class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Addition : ",self.a+self.b)

    def sub(self):
        print("Subtraction : ",self.a-self.b)
    def Mul(self):
        print("Mul : ",self.a*self.b)
    def div(self):
        print("Division : ",self.a/self.b)

a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
obj=Calc(a,b)
obj.add()
obj.sub()
obj.Mul()
obj.div()