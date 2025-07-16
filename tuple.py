      #CREATING TUPLES

# data=(0,1,2,3,2,3,4,1,2)
# print(data)
         
         #EMPTY TUPLE

# my_tuple=()
# print(my_tuple)
            
            #NESTED TUPLE

# my_tuple=("mouse",[3,5,8],(1,2,3))
# print(my_tuple)
       
       #INDEXING

# letters=('P','R','O','G','R','A','M','I','Z')
# print(letters[5])
# print(letters[3])

       #NEGATIVE INDEXING

# letters=('p','r','o','g','r','a','m','i','z')
# print(letters[-1])
     #slicing
# print(letters[1:4])
# print(letters[:7])
# print(letters[:-7])
# print(letters[-7:])

    #REPETITION TUPLES

# fruit=('apple','orange')
# fruit=fruit*3
# print(fruit)

      #TUPLE METHODS

# fruit=('A','P','P','L','E')
# print(fruit.count('P'))
# print(fruit.index('A'))

     #ITERATING THROUGH A TUPLE

# languages=('python','C++','java')
# for i in languages:
#     print(languages)
# print('java' in languages)

      #SOME EXAMPLES OF TUPLE

# text="programming"
# print(text[0],text[-1])

# reversed_text=text[::-1]
# print(reversed_text)

# print(text.count("m"))

# sentence="python is fun to learn"
# print(sentence.replace(" ","_"))

# word="madam"
# print(word==word[::-1])

# num=[i for i in range(1,21) if i%2==0]
# print(num)

# days=('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
# print(days[0])
# print(days[1:6])
# print(days.index('wednesday'))

# d letter
# for row in range(7):
      # for col in range(5):
      #       if (col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
      #        print("*",end="")
      #       else:
      #             print(end=" ")
      # print()


               #SETS

# a=set()
# print(type(a))
# set1={1,6,4,'abc'}
# print(type(set1))

# days=set(['monday','tuesday','wednesday','thursday'])
# print(days)
# print(type(days))
# for i in days:
#       print(i)

            #USING add() METHOD

# months=set(["january","february","march","april","may"])
# print(months)
# months.add("june")
# print(months)

           #USING update() METHOD

# months=set(["january","february","march","april","may"])
# print(months)
# months.update(["june","july"])
# print(months)

           #USING discard() METHOD

# months=set(["january","february","march"])
# print(months)
# months.discard("march")
# print(months)

            #USING remove() METHOD

# months=set(["january","february","march"])
# print(months)
# months.remove("january")
# print(months)
               
               #UNION OF TWO SETS


# days1={"monday","tuesday","wednesday","thursday"}
# days2={"friday","saturday","sunday"}
# print(days1|days2)

               #INTERSECTION OF TWO SETS

# days1={"monday","tuesday","wednesday"}
# days2={"sunday","thursday","monday"}
# print(days1&days2)

              #SET COMPARISONS

# days1={'monday','tuesday','wednesday','thursday'}
# days2={'monday','tuesday'}
# days3={'monday','tuesday','friday'}
# print(days1>days2)    #DAYS1 IS SUPERSET OF DAYS2
# print(days1<days2)    #DAYS1 IS NOT THE SUBSET OF DAYS2
# print(days1==days2)


# days=['monday','monday','tuesday','wednesday']  
# set1=set(days)
# print(set1)


# b=set()
# for i in range(5):
#       a=int(input("Enter number"))
#       b.add(a)
# print(b)


# b=set()
# a=input("Enter the string : ")
# for i in a:
#       if i in 'aeiouAEIOU':
#             b.add(i)
# print(b)

# fruits=set(['apple','orange','kiwi','mango'])
# for i in fruits:
#       if len(set(i))==len(i):
#             print(i)

