# f=lambda a,b:a+b
# print(type(f))
# print(f(45,12))



# numbers=[45,23,5,6]
# def Fun(num):
#     return num*2
# print(list(map(Fun,numbers)))



numbers=[23,6,7,10,3,16]
# print(list(map(lambda x:x*2,numbers)))

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
# print(list(map(is_even, numbers)))           

# print(list(filter(is_even, numbers)))       #USING FILTER()



        #  FACTORIAL


from functools import reduce
s=reduce(lambda a,b:a*b,range(1,6))
# print(s)

           
           #SQUARE

        
square=lambda a: a * a
# print(square(6))

        
       #CHECK ODD OR EVEN

num=lambda x: "Even" if x % 2==0 else "Odd"
# print(num(7))

      
             #MAXIMUM OF TWO NUMBERS

num=lambda a,b: a if a>b else b
# print(num(7,2))

     
            #TO CHECK IF LETTER STARTS WITH "A"

string=lambda s:"true" if s[0]=="A" or s[0]=="a" else "false" 
# print(string("abcd"))


           #RETURNS THE MAX NUMBER

def max_(list):
    return max(list)
# print(max_([3,67,98,56,76]))


          #check vowels in a string

def string_(s):
    count=0
    vowels="AEIOUaeiou"

    for i in s:
        if i in vowels:
            count=count+1
    return count
        
# print(string_("apple"))


          # even number from a list


def even(list):
    return [x for x in list if x%2==0]
# print(even([10,21,31,42]))

       #power of a number

def power(a, b):
    num=1
    for i in range(b):
        num=num*a
    return num
# print(power(2,3))


               #REVERSE A STRING

def rev(s):
    if len(s)==0:
        return s 
    else:
       return rev(s[1:])+s[0]
# print(rev("python"))


        #TO CHECK IF A NUMBER IS PALINDROME


def palindrome(n):
   
    if n==n[::-1]:
       return True
    else:
        return False
print(palindrome("121"))