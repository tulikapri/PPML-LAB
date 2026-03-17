m = int(input("Enter the starting number (m): "))
n = int(input("Enter the ending number (n): "))
num_list = []
for i in range(m, n + 1):
    num_list.append(i)
total = 0
largest = num_list[0]
smallest = num_list[0]
for i in num_list:
    total += i
    for j in num_list:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
average = total / len(num_list)
print("List:", num_list)
print("Sum:", total)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)