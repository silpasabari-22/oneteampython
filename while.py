# count=int(input("Enter the number "))
# while count>=1:
#     if(count%2==0):
#         print(count)
#     count-=1

# sum=0
# a=int(input("Enter the number "))
# while a!=-1:
#     sum=sum+a 
#     a=int(input("Enter the number "))
# print(sum) 

      #sum of digits
     
# num=int(input("Enter the number "))
# sum=0
# while num>0:
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print(sum)

           #palindrome
num=int(input("Enter a number "))
a=num
j=0
while num>0:
      rem=num%10
      j=(j*10)+rem
      num=num//10
      if a==j:
         print("It is a palindrome")
      else:
           print("It is not a palindrome")

        #count the number of digits







