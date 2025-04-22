# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print(f"{self.name} says woof!")

# dog1 = Dog("Nina", 4)
# dog2 = Dog("Kuci", 6)
# dog3 = Dog("Wolf", 2)

# dog1.bark()
# dog2.bark()
# dog3.bark()

# class Student:
#     def __init__(self, name, percentage):
#         self.name = name
#         self.percentage = percentage
    
#     def Show(self):
#         print(f"{self.name} has got {self.percentage}%")

# stud1 = Student('Blend', 92)

# stud1.Show()

class MyClass:
    def __init__(self):
        self.__private_variable = "__private_variable"
        self.__protected_variable = "protected variable"
    def __private_MyMethod(self):
        print("This is private method")
    def __protected_Method(self):
        print("Protected Method")
    

myclass = MyClass("")