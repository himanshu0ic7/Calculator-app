from function import add,mul,sub
from divide import divide
def main():
    print('''
        1. Enter 1 for addition
        2. Enter 2 for subtraction
        3. Enter 3 for Multiplication
        4. Enter 4 for division
''')
    choice=int(input("Enter your choice: "))
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    if choice==1:
        print(add(a,b))
    elif choice==2:
        print(sub(a,b))
    elif choice==3:
        print(mul(a,b))
    elif choice==4:
        print(divide(a,b))

if __name__=="__main__":
    main()