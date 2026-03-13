p=float(input("Enter the principal: "))
r=float(input("Enter the rate: "))
t=float(input("Enter the time : "))
si=(p*r*t)/100
A=p*(1+(r/100))**t
CI=A-p
print("Simple Interest : ",si)
print("Compound Interest : ",CI)