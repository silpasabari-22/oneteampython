# n=4
# for i in range(n):
#     print(" " * (n-i), end="")
#     num=1
#     for j in range(i+1):
#         print(num,end=" ") 
#         num=num*(i-j)//(j+1)
#     print()  
        
#Hollow full pyramid:
# n=4
# for i in range(n):
#     print(" " * (n - i -1), end="")

#     for j in range(2 * i + 1):
#         if j==0 or j==2 * i or i==n-1:
#               print("*", end="")  
#         else:
#              print(" ", end="")
#     print()          

# hollow inverted full pyramid:
# n=3
# for i in range(n):
#     print(" " * i, end="")
    # for j in range(2 * (n - i) - 1):
    #     if i == 0 or j == 0  or j == (2 * (n - i) - 2):
    #           print("*", end="")  
    #     else:
    #          print(" ", end="")
    # print()          

#HOLLOW Diamond Pyramid:
# n=4
# for i in range(n):
#     print(" " * (n - i - 1), end="")
#     for j in range(2 * i + 1):
#         if j==0 or j==2 * i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print() 
# for i in range(n - 2, -1,-1):
#     print(" " * (n - i - 1), end="")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



#A letter
# n=5
# for i in range(n):
#     for j in range(n):
        # if((j==0 or j==n-1) and i!=0
        # or i==0 and j > 0 and j < n-1 or i ==n//2):
        #   print("*",end="")
        # else:
        #     print(" ",end="")  
    # print()       

    # diamond pattern 
# n=5
# for i in range(0,n-1):
#   for j in range(0,n-i):
#     print("",end=" ")
#   for k in rnge(0,i+1):
#     print("* ",end=" ")
#   print()
# n=6

# for i in range(0,n):
#   for j in range(i+1):
#     print(" ",end="")
#   for k in range(n-i):
#       print("* ", end="")
#   print()

# hollow full pyramid
 
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#                print("",end=" ")
    # for k in range(0,n):
    #       if(k==0 or k==i or j==0):
    #           print("",end=" ")
    #       else:
    #             print(" ",end=" ")

    # print()

#     d letter
# def print_pattern(n):
#  for row in range(n):
#   for coloumn in range(n-2):
#     if(row == 0 or row == n-1) and (column > 0 and column < n-3) \
#   or column == 0 or column == n-3 and row != n-1:
#   print("*",end="")
#   else:
#     print(" ",end="") 
#   print()
# num = int(input("Enter the size \t"))
# if num < 8:
#   print("Enter a number atleast 8")
# else:
#   print_pattern(num)