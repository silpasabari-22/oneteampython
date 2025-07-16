         #IF STATEMENT

# i=4
# if(i % 2 == 0):
#    print("The number is even")
# print("not in if")


# age = 20
# if age >= 18:
#     print("eligible to vote")


#  number = 10
#  if number > 0:
#      print("The number is positive.")



# a=float(input("Enter a number :"))
# if a>0:
#     print("The number is positive")


# a=int(input("Enter a number :"))
# if a%5==0:
#     print("The number is divisible by 5")


# vowel=input("Enter a character ")
# if(vowel in "aeiouAEIOU"):
#     print("This is a VOWEL")



#IF ELSE STATEMENT

# a=int(input("Enter a number "))
# if a%2==0:
#     print("The number is Even")
# else:
#     print("The number is Odd")


# age=int(input("Enter your age "))
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")


# a=int(input("Enter first number "))
# b=int(input("Enter second number "))
# if a>b:
#     print("first number is greatest")
# else:
#     print("second number is greatest")


#  year=int(input("Enter a year :"))
#  if year%4==0:
#     print("This year is leap year")
#  else:
#      print("This year is not leap year")


#write a python program to calculate the water bill based on the number of units consumed

# units=int(input("Enter the total units consumed "))
# bill=0
# if units<=100:
#     bill=units*5
# elif units<=200:
#     bill=500 + ((units-100)*8)
# else:
#     bill=1300+((units-200)*10)      #(100*5)+(100*8)
# print("Total water bill:", bill)







# i=10
# if i<15:
#     print("i is smaller than 15")
#     print("i am in if block")
# else:
#     print("i is greater than 15")
#     print("i am in else block")
# print("i am not in if and not in else block")


# i=10
# if i==10:
#     if i<15:
#         print("i is smaller than 15")
#     if i<12:
#         print("i is smaller than 12 too")
#     else:
#         print("i is greater than 15")


# i=25
# if i==10:
#     print("i is 10")
# elif i==15:
#     print("i is 15")
# elif i==20:
#     print("i is 20")
# else:
#     print("i is not present")



a=int(input("Enter the mark "))

if a>100:
    print("INVALID")
elif a>90:
    print("A Grade")
elif a>80:
    print("B Grade")
elif a>70:
    print("C Grade")
elif a>60:
    print("PASS")
else:
    print("you are failed")