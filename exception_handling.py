     #SYNTAX ERROR

     #TYPE ERROR

# x=5
# y="hello"
# try:
#     z=x+y 
# except TypeError:
#     print("Error:cannot add an int and a str")


# x=5
# y="hello"
# try:
#     z=x+y 
# except Exception as e:
#     print(e)


#TRY AND EXCEPT STATEMENT - CATCHING EXCEPTIONS

# a=[1,2,3]
# try:
#      print("second element = ",a[1])
#      print("Fourth element = ",a[3])
# except:
#      print("An error occured")


        #CATCHING SPECIFIC Exceptions

# def fun(a):
#      if a<4:
#           b=a/(a-3)
#      print("Value of b = ",b)
# try:
#      fun(3)
# except ZeroDivisionError:
#      print("ZeroDivisionError Occured and Handled")
# except NameError:
#      print("NameError Occured and Handled")


         #Finally keyword in python 