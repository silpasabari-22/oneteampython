





# prime_numbers=[2,3,5,7]
# removed_element=prime_numbers.pop(2)
# print('Removed Element :',removed_element)
# print('Updated List:',prime_numbers)


             #PRINT EVEN 

# var=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(var)):
#     if i<=len(var)-1:
#         if var[i]%2!=0:
#             var.pop(i)
# print('list:',var)




# c=[]
# while True:
#     print("1.add")
#     print("2.remove")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         a=int(input("Enter the  no: "))
#         c.append(a)
#         print(c)
#     elif choice==2:
#         b=int(input("Enter the value: "))
#         for i in range(len(c)):
#             if i<=len(c)-1:
#                 if c[i]==b: 
#                    c.pop(i)
#                    print(c)


            #del()

# languages=['python','swift','C++','C','java','Rust','R']
# del languages[1]
# print(languages)
# del languages[-1]
# print(languages)
# del languages[0:2]
# print(languages)


       #USING remove()

# languages=['python','swift','C++','java','Ruat','R']
# languages.remove('python')
# print(languages)

       #USING reverse()

# primenumbers=[2,3,5,7]
# primenumbers.reverse()
# print('Reversed List:',primenumbers)

       #REPETITION


# list1=[12,14,17,19]
# l=list1*2
# print(l)

       #CONCATINATION AND LEN(LIST)

# list1=[12,14,16,18,20]
# list2=[9,10,23,56,84]
# l=list1+list2
# print(l)
# a=print(len(list1))

        #ITERATION AND MEMBERSHIP

# list=[3,1,5,12,27]
# for i in list:
#     print(i)

# list=["john","anu","anshi","appu"]
# for i in list:
#      print(i)

          
          #max() and min()


# list1=[103,34,567,184]
# print(max(list1))
# list2=['dharshana','anu','silpa']
# print(max(list2))

# list1=[2,45,678,1]
# print(max(list2))
# print(min(list1))

       
        #INTERSECTION 


# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# intersection1=set(list1).intersection(list2)
# print(intersection1)

# intersection2=set(list1)&set(list2)
# print(intersection2)

    #INTERSECTION USING CODE

# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# list3=[]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i]==list2[j]:
#             list3.append(list2[j])
# print(list3)

       #FIND MAXIMUM VALUE IN LIST USING CODE

# list1=[33,54,642,24,23]
# greatest=list1[0]
# for i in range(len(list1)):
#     if list1[i]>greatest:
#         greatest=list1[i]

# print(greatest)

          #MINIMUM

# list1=[33,54,642,24,23]
# greatest=list1[0]
# for i in range(len(list1)):
#     if list1[i]<greatest:
#         greatest=list1[i]

# print(greatest)

         #MAXIMUM LENGTH OF STRING

list1=['jyothi','anusree','dhrishya','silpa']
l=[]
for i in range(len(list1)):
       a = len(list1[i])
       l.append(a)
# print(l)
greatest=l[0]
string=list1[0]
for j in range(len(l)):
       if l[j] < greatest:
              greatest=l[j]
              string=list1[j]
print(greatest)
print(string)               

               #LIST COMPREHENSION

# numbers=[1,2,3,4,5]
# a=[x**2 for x in numbers]
# print(a)

       # MATRIX USING LIST COMPREHENSION

# matrix=[[j for j in range(3)]for i in range(3)]
# print(matrix)

