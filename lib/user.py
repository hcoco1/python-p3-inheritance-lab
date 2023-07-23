#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        


#The given code defines three classes: User, Student, and Teacher, demonstrating inheritance and method overriding in Python. Let's go through each class and its methods to understand the code:
#User Class:
#The User class has a constructor (__init__ method) that takes first_name and last_name as parameters and initializes the self.first_name and self.last_name attributes with the provided values.
#This class serves as the base class or parent class for the Student and Teacher classes, and it contains common attributes and behaviors that both student and teacher objects will inherit.
#Student Class (Inherits from User):
#The Student class is a subclass of the User class, inheriting all the properties and methods from the User class.
#The __init__ method of the Student class overrides the parent class's (User) __init__ method using super().__init__(first_name, last_name). It calls the parent class's constructor to initialize the self.first_name and self.last_name attributes inherited from the parent class.
#The Student class also has an additional attribute, knowledge, which is initialized as an empty list for each student. This attribute will be used to store knowledge learned by students.
#The learn() method is defined in the Student class, which takes new_knowledge as a parameter. When called, it appends the new_knowledge string to the student's self.knowledge list.
#Teacher Class (Inherits from User):
#The Teacher class is also a subclass of the User class, inheriting the properties and methods from the User class.
#The __init__ method of the Teacher class also overrides the parent class's (User) __init__ method using super().__init__(first_name, last_name). It calls the parent class's constructor to initialize the self.first_name and self.last_name attributes inherited from the parent class.
#The Teacher class has an additional attribute, knowledge, which is a list of predefined strings representing the knowledge that the teacher has.
#The teach() method is defined in the Teacher class. When called, it returns a random element from the teacher's self.knowledge list using the random.randint() method.
#In summary, this code demonstrates inheritance in Python, where the Student and Teacher classes inherit attributes and methods from the User class. It also shows method overriding, where the Student and Teacher classes override the __init__ method of the User class to add their own specific attributes (knowledge). The teach() method in the Teacher class showcases how a specific behavior can be added to the derived class while using the parent class's attributes.