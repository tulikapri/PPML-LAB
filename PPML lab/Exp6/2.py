dict1 = {}
n = int(input("Enter number of elements: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value
dict2 = {}
for key, value in dict1.items():
    dict2[value] = key
print("\nFirst Dictionary:")
print(dict1)
print("\nSecond Dictionary (reversed dictionary):")
print(dict2)