while True:

    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice : "))
    a=int(input("Enter the number : "))
    b=int(input("Enter the number : "))
   
    from calc import add,sub,mul,divi 
    if choice==1:
        print(add(a,b))
  
    elif choice==2:
        print(sub(a,b))     
       
    elif choice==3:    
        print(mul(a,b))

    elif choice==4:
        if b!=0: 
            print(divi(a,b))
    else:         
        print("please enter a valid input from choices given")
        c=input("Do you wish to continue (yes/no)? ")
    if c.lower()!="yes":
        break


