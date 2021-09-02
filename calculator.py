n1 = int(input("enter any number: "))
b = input("enter +,-,*,/ operator: ")
n2 =int(input("enter number: "))
if b=='+':
    print(n1+n2)
elif b=='-':
    print(n1-n2)
elif b=='*':
    print(n1*n2)
elif b=='/':
    print(n1/n2)
else:
    print("error! please check again!!!!")