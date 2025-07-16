        #PALIANDROME

# num=int(input("Enter the number "))
# length=len(str(num))
# # print(length)
# j=0
# if num>0:
#     for i in range(length):
#         rem=num%10
#         j=(j*10)+rem
#         num=num//10
#     print(j)
# else:
#     print("Not a positive ")+

         #MULTIPLICATION

# num=int(input("Enter the number "))
# for i in range(1,11):
#         print(f"{i}*{num}={i*num}")


         #MULTIPLICATION WITH LIMIT

# num=int(input("Enter the number "))
# j=int(input("Enter the limit "))
# for i in range(1,j+1):
#     print(f"{i}*{num}={i*num}")


           #REVERSE STRING

# string=input("enter a string:")
# reverse=""
#for i in text:
#     reverse=i+reverse
# print("reversed string is : ",reverse)

# a=text[::-1]
# print(a)





           # PYRAMIDS



       #1 TO 25 
# n=5
# a=1
# for i in range(0,n):
#         for j in range(0,n):
#             print(a,end="  ")
#             a=a+1
#         print()

        #1 to 15 TRIANGLE
# n=5
# a=1
# for i in range(0,n):
#         for j in range(0,i+1):
#             print(a,end=" ")
#             a=a+1
#         print()

        #RIGHT HALF TRIANGLE

# n=5
# for i in range(0,n):
#         for j in range(0,i+1):
#                 print("*",end=" ")
#         print() 

       
        #INVERTED RIGHT HALF PYRAMID

# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("*",end=" ")
#         a=a+1
#     print()


       #LEFT HALF TRIANGLE

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
        
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()

       #FULL PYRAMID

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")
        
#     for k in range(0,i+1):
#         print("* ",end=" ")
#     print()


       #INVERTED LEFT HALF PYRAMID

# n=5
# a=1
# for i in range(0,n):
#     for j in range(i):
#         print(" ", end=" ")

#     for k in range(n - i):
#         print("*", end=" ")
#         a+=1
#     print()

        #INVERTED FULL PYRAMID

# n=5
# for i in range(0,n):
#         for j in range(i):
#                 print("",end=" ")
#         for k in range(0,n-i):
#                 print("*",end=" ")
#         print()



                          #FLOYD'S TRIANGLE



# n=5
# for i in range(0,n):
#         a=i+1
#         for j in range(0,i+1):
#          a=i+1
#               print(a,end=" ")
#         print()


                    #DIAMOND

# n=4
# for i in range(0,n-1):
#         for j in range(0,n-i):
#                print("",end=" ")
#         for k in range(i+1):
#                print("*",end=" ")
#         print()

# n=4
# for i in range(n):
#         for j in range(i+1):
#                 print(" ",end="")
#         for k in range(0,n-i):
#                 print("* ",end= "")
#         print()


                       #RHOMBUS


# n=5
# for i in range(n):
#         for j in range(n+i):
#                 print(" ",end=" ")
#         for k in range(n-1):
#                 print("* ",end=" ")              
#         print()


                   #HOURGLASS PATTERN


# n=5
# for i in range(n):
#         for j in range(i+1):
#                 print(" ",end="")
#         for k in range(0,n-i):
#                 print("* ",end="")
#         print()                
# n=5
# for i in range(0,n):
#         for j in range(0,n-i):
#                 print("",end=" ")
#         for k in range(i+1):
#                 print("*",end=" ")
#         print()



                 #HOLLOW FULL PYRAMID



# n=5
# for i in range(0,n):
#         for j in range(0,n-i):
#                 print("",end=" ")
#         for k in range(0,n):
#                if(k==0 or k==i or j==0):
#                   print("*",end=" ")
#                else:
#                         print(" ",end=" ")
#         print()


              #HOLLOW INVERTED TRIANGLE


# n=5
# for i in range(0,n):
#         print(" " * i, end="")
#         for j in range(2 * (n-i) -1):
#                 if j==0 or j==(2*( n-i)-2) or i==0:
#                          print("*",end="")
#                 else:
#                       print(" ",end="")
#         print()


                #HOLLOW DIAMOND PYRAMID








                #HOLLOW SQUARE PYRAMID

# n=5
# for i in range(0,n):
#         for j in range(0,n):
#                 if i==0 or i==n-1 or j==0 or j==n-1:
#                    print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()


                #PASCALS TRIANGLE

# n=4
# for i in range(n):
#     print(" " * (n-i), end="")
#     num=1
#     for j in range(i+1):
#         print(num,end=" ")
#         num=num*(i-j)//(j+1)
#     print()

         
