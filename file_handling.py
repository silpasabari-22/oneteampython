# f=open('sample.py','x')

# f=open('sample.py','a')
# f.write("welcome to this page")
# f.write("\nHello..!")
# f.close()

# f=open('sample.py','r')
# for i in f:
    # print(i)
# print(f.readline())
# print(f.readline())
# print(f.read())

# with open("sample.py") as f:
#     data=f.read()
# print(data)

# print(f.read(5))

with open("sample.py","r") as f:
    data=f.readlines()
for i in data:
    word=i.split()
    print(word)