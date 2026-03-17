d = int(input("Enter a digit (0-6): "))

days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]

if 0 <= d <= 6:
    print(days[d])
else:
    print("Invalid input")