#IF STATEMENT

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

units=int(input("Enter the total units consumed "))
bill=0
if units<=100:
    bill=units*5
elif units<=200:
    bill=500 + ((units-100)*8)
else:
    bill=1300+((units-200)*10)      #(100*5)+(100*8)
print("Total water bill:", bill)