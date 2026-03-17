def simple_interest(p, r, t):
    return (p * r * t) / 100
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))
si = simple_interest(principal, rate, time)
print("Simple Interest is:", si)