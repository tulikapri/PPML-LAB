a=0
b=0
sum_even=0
print("Fibonacci series upto 1000: ")
while a<=1000:
    print(a, end=" ")
    if a%2==0:
        sum_even=sum_even+a
    c=a+b
    a=b 
    b=c
    print("\nSum of even_valued Fibonacci terms: ", sum_even)