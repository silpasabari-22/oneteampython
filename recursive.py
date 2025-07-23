
            #RECURSION

      #FACTORIAL

def fact(num):
      if num==1:
          return num
      else:
            return num*fact(num-1)
# print(fact(5))



def fun():
      print("hello")
      fun()
# fun()


      #TO PRINT NUMBERS FROM N TO 1

# def num(n):
#     if n==0:
#       return 
#     else: 
#       print(n)
#       return num(n-1)
# num(4)

        #TO SUM OF FIRST N NATURAL NUMBERS


# def sum(n):
#     if n==0:
#       return 0
#     else: 
      
#       return n+sum(n-1)
# print(sum(4))

      #TO SUM OF DIGITS

# def summ(n):
#       if n==0:
#             return 0
#       else:
          
#             return (n % 10) + summ(n//10)
# print(summ(16))

      #TO REVERSE A STRING

def rev(s):
      if len(s)==0:
            return s
      else:
            return rev(s[1:])+s[0]
print(rev("python"))





