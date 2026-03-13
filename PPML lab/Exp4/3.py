a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))    
while b!=0:
    a,b=b,a%b
while c!=0:
    a,c=c,a%c
print("GCD is : ",a)    