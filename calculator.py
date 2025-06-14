def Add(x,y):
    return x+y;

def Sub(x,y):
    return x-y;

def Mul(x,y):
    return x*y;

def Div(x,y):
    if(y == 0):
        return "Division Not possible";
    else:
        return x/y;

print("Welcome to Calculator program for Basic operations (Only for 2 numbes) : ");

while True:
    print("---------------------------------------------- \n");
    print("Enter 1 to Add two numbers");
    print("Enter 2 to Subtract two numbers");
    print("Enter 3 to Multiply two numbers");
    print("Enter 4 to Divide two numbers");
    print("Enter 5 to Exit ");

    choice = int(input("Enter the choice : "));
    if(choice == 1):
        num1 = int(input("Enter the 1st number :"));
        num2 = int(input("Enter the 2nd number :"));
        print("Result : ",Add(num1,num2));

    elif(choice == 2):
        num1 = int(input("Enter the 1st number :"));
        num2 = int(input("Enter the 2nd number :"));
        print("Result : ",Sub(num1,num2));

    elif(choice == 3):
        num1 = int(input("Enter the 1st number :"));
        num2 = int(input("Enter the 2nd number :"));
        print("Result : ",Mul(num1,num2));

    elif(choice == 4):
        num1 = int(input("Enter the 1st number :"));
        num2 = int(input("Enter the 2nd number :"));
        print("Result : ",Div(num1,num2));

    elif(choice == 5):
        break;

    else:
        print("Invalid Choice");
    
   
    
