total = 0

for i in range(1, 6):
    m = int(input("Enter marks: "))
    total += m

per = (total / 250) * 100
print("Percentage =", per)

if per >= 90:
    print("Grade = O")
elif per >= 80:
    print("Grade = E")
elif per >= 70:
    print("Grade = A")
elif per >= 60:
    print("Grade = B")
else:
    print("Fail")