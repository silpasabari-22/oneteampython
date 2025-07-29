# class Employee:
#     id=10
#     name="john"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# del emp.id
# del emp.name           #DELETE THE OBJECT
# emp.display()


               #CREATING THE CONSTRUCTOR IN PYTHON

# class car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year 
#     def display(self):
#         print(self.modelname,self.year)
# c1=car("Toyota",2016)
# # del c1.modelname
# c1.display()


# class Employee:
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp1=Employee("john",101)
# emp2=Employee("David",102)
# emp1.display()
# emp2.display()

           #NON-PARAMETERIZED CONSTRUCTOR

# class Student:
#     def __init__(self):
#         print("This is non parameterized constructor")
#     def show(self,name):
#         print("Hello",name)
# student=Student()
# student.show("john")


# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("john",101,22)
# print(getattr(s,'name'))

# setattr(s,"age",23)
# print(getattr(s,'age'))

# print(hasattr(s,'id'))

# delattr(s,'age')

# print(s.age)    


           #INHERITANCE


    #SINGLE INHERITANCE

# class Animal:   
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.bark()
# d.speak()


    #MULTI LEVEL INHERITANCE

# class Animal:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# class Childdog(Dog):
#     def eat(self):
#         print("Eating braed")
# d=Childdog()
# d.bark()
# d.speak()
# d.eat()


    #MULTIPLE INHERITANCE

# class Calculation1:
#     def summation(self,a,b):
#         return a+b
# class Calculation2:
#     def multiplication(self,a,b):
#         return a*b 
# class Derived(Calculation1,Calculation2):
#     def Divide(self,a,b):
#         return a/b 
# d=Derived()
# print(d.summation(20,10))
# print(d.multiplication(20,10))
# print(d.Divide(20,10))



     #HIERARCHICAL INHERITANCE

# class Parent:
#     def fun1(self):
#         print("This function is in parent class")
# class Child1(Parent):
#     def fun2(self):
#         print("This function is in child1 class")
# class Child2(Parent):
#     def fun3(self):
#         print("This function is in the child2 class")
# d=Child2()
# d.fun1()
# d.fun3()


      #HYBRID INHERITANCE


# class A:
#     def fun1(self):
#         print("feature from class a")
# class B(A):
#     def fun2(self):
#         print("feature from class B")
# class C(A):
#     def fun3(self):
#         print("feature from class c")
# class D(B,C):
#     def fun4(self):
#         print("feature from class d")
# obj=D()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# obj.fun4()



#           #POLYMORHISM Eg:METHOD OVERRIDING

    #    EXAMPLE 1

# class Bank:
#     def getroi(self):
#         return 10
# class SBI(Bank):
#     def getroi(self):
#         return 7
# class ICICI(Bank):
#     def getroi(self):
#         return 8
# b1=Bank()
# b2=SBI()
# b3=ICICI()
# print("Bank rate of interst:",b1.getroi())
# print("SBI rate of interest:",b2.getroi())
# print("ICICI rate of interest:",b3.getroi())

        # EXAMPLE 2

# class Bird:
#     def intro(self):
#         print("There are many types of birds")
#     def flight(self):
#         print("Most of the birds can fly but some cannot")
# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly")
# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly")
# b=Bird()
# s=sparrow()
# o=ostrich()
# b.intro()
# b.flight()
# s.intro()
# s.flight()
# o.intro()
# o.flight()


              #ENCAPSULATION

   #PROTECTED MEMBERS

# class Base:
#     def __init__(self):
#         self._a=2
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling protected member of base class : ",self._a)
#         self._a=3
#         print("Calling modified protected member outside class : ",self._a)
# obj1=Derived()
# obj2=Base()
# print("Accessing protected member of obj1:",obj1._a)
# print("Accessing protected member of obj2:",obj2._a)

    #PRIVATE MEMBERS

# class Base:
#     def __init__(self):
#         self.a="HELLO"
#         self.__c="World"

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of base class")
#         print(self.__c)
# obj1=Base()
# print(obj1.a)



         #ABSTRACTION


from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod 
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Boow!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
d=Dog()
c=Cat()
print(d.make_sound())
print(c.make_sound())



