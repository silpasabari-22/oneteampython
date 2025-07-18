# f=lambda a,b:a+b
# print(type(f))
# print(f(45,12))



# numbers=[45,23,5,6]
# def Fun(num):
#     return num*2
# print(list(map(Fun,numbers)))



# numbers=[23,6,7,10,3,16]
# print(list(map(lambda x:x*2,numbers)))

# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False

# print(list(map(is_even,numbers)))            #USING MAP()

# print(list(filter(is_even, numbers)))       #USING FILTER()



# numbers=[13,2,5,68,70]
# print(list(filter(lambda num:True if num%2==0 else False,numbers)))



from functools import reduce
s=reduce(lambda a,b:a*b,range(1,6))
print(s)