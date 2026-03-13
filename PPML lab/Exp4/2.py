num=int(input("Enter a number: "))
o=2
is_prime="Yes"
while i<num:
    if num%i==0:
        is_prime="No"
        i=i-1
    if is_prime=="Yes":
        print("Itis a prime number")  
    else:
        print("It is not a prime number")       