
def add(x,y):
    ans=x+y
    print(f"sum of {x} amd {y} is {ans}")

def sub(x,y):
    ans=x-y
    print(f"subtraction of {x} and {y} is {ans}")

def mul(x,y):
    ans=x*y
    print(f"multiplication of {x} and {y} is {ans}")

def div(x,y):
    ans=x/y
    print(f"division of {x} and {y} is {ans}")

while True:
    a=int(input("Enter the number : "))
    b=int(input("Enter the number : "))
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice : "))
    if choice==1:
        add(a,b)
    elif choice==2:     
        sub(a,b)
    elif choice==3:    
        mul(a,b)
    elif choice==4:
        if b!=0:
           div(a,b)
    else:         
        print("please enter a valid input from choices given")
    c=input("Do you wish to continue (yes/no)? ")
    if c.lower()!="yes":
         break