          #CREATE A DICTIONARY

# capital_city={"Nepal":"kathmandu","italy":"rome"}
# print(capital_city)
# for i in capital_city:
#      print(capital_city[i])

     #ADD ELEMENTS TO A PYTHON DICTIONARY

# capital_city={"nepal":"kathmandu","England":"london"}
# print("Initial dictionary :",capital_city)
# capital_city["nepal"]="Tokyo"
# print("Updated Dictionary: ",capital_city)

      #CHANGE VALUE OF DICTIONARY

# student_id={111:"Eric",112:"kyle",113:"Butters"}
# print("Initial dictionary: ",student_id)
# student_id[112]="Stan"
# print("Updated dictionary: ",student_id)

      #ACCESSING ELEMENTS

# student_id={111:"Eric",112:"kyle",113:"butters"}
# print(student_id[111])
# print(student_id[113])

      #REMOVING ELEMENTS 

# student_id={111:"Eric",112:"kyle",113:'butters'}
# print("Initial dictionary: ",student_id)
# del student_id[111]
# print("Updated dictionary: ",student_id)

     #ITERATING THROUGH A DICTIONARY

# squares={1:1,3:9,5:25,7:49,9:81}
# for i in squares:
#     print(squares[i])


# square={}
# for i in range(1,11):
#      square[i]=i*i
# print(square)

# keys=['name','age','city','state']
# value=['Alice','30','New York']
# my_dict=dict(zip(keys,value))
# print(my_dict)



                   #FUNCTIONS



         #USER-DEFINED FUNCTION


# def square(num):
#       return num**2
# object=square(6)
# print("The square of the given number is : ",object)



# def square(num):
#       print(num**2)
# square(6)


          #FIND LENGTH OF STRING


# def a_function(string):  
#      return len(string)

# print(a_function("Functions"))
# print(a_function("Python"))


     #WITH ARGUMENT WITH RETURN TYPE

# def square(num):
#       return num*num
# result=square(5)
# print("Square:",result)

      #WITH ARGUMENT WITHOUT RETURN TYPE

# def greet(name):
#       print("Hello",name+"!")
# greet("Anu")

      #WITHOUT ARGUMENT WITH RETURN TYPE

# def get_message():
#       return "Welcome to python programming!"
# msg=get_message()
# print(msg)

      #WITHOUT ARGUMENT WITHOUT RETURN TYPE

# def print_numbers():
#       for i in range(1,6):
#             print(i)
# print_numbers()


           #FUNCTION ARGUMENTS

      #DEFAULT ARGUMENTS

# def function(n1,n2=20):
#       print("number 1 is :",n1)
#       print("number 2 is : ",n2)
# print("passing only one argument")
# function(30)


       #KEYWORD ARGUMENTS

# def function(n1,n2):
#       print("number 1 is : ",n1)
#       print("number 2 is : ",n2)
# print("Without using keyword")
# function(n2=50,n1=20)

           #ODD OR EVEN

# def is_even(num):
#       if num%2==0:
#             print(num,"is even")
#       else:
#             print(num,"is even")
# a=int(input("Enter the number : "))
# is_even(6)


# def is_even(num):
#       if num%2==0:
#           return True
#       else:
#           return False
# a=int(input("Enter the number : "))
# c=is_even(a)
# if c:
#    print(a,"is even")


        #FACTORIAL OF A NUMBER

# def find_fact(num):

#       fact=1
#       for i in range(1,num+1):
#             fact=fact*i
#       return fact
# a=int(input("Enter the number : "))
# f=find_fact(a)
# print(f"factorial of {a} is {f}")

            #LEAP YEAR

# def is_leapyear(num):
#       if num%4==0:
#             return True
#       else:
#             return False
# a=int(input("Enter the year  : "))
# yr=is_leapyear(a)
# if yr:
#    print(a,"is a leap year")
 
           #DISPLAY FUNCTION

# def display(name,age):
#       print(f"my name is {name} and {age} years oldS")

# display(name="silpa",age=20)



# def fun(*s):
#     print(sum(s))

# fun(23,6,56,82,4,15)


# def display(**a):  
#     print(f"my name is {a['name']} and i choose {a['course']}")

# display(name="silpa", age=20, course="python")


        #GLOBAL FUNCTION()


# a=10
# def global_fun():
#       global a
#       a+=11
#       print(a)
# global_fun()


            #RECURSION


# def fact(num):
#       if num==1:
#           return num
#       else:
#             return num*fact(num-1)
# print(fact(5))



# def fun():
#       print("hello")
#       fun()
# fun()


         #FIBONACCI SERIOUS

first,second=0,1
print(first,second,end=" ")
for i in range(8):
      third=first+second
      print(third,end=" ")
      first,second=second,third

