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

class Student:
    def __init__(self):
        print("This is non parameterized constructor")
    def show(self,name):
        print("Hello",name)
student=Student()
student.show("john")
    