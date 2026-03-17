numbers = []  

n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
unique_numbers = list(set(numbers))
unique_numbers.sort()
print("List after removing duplicates and sorting:")
print(unique_numbers)
