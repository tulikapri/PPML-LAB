fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Fruits displayed in reverse order with length:")
for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i], "- Length:", len(fruits[i]))
reverse_fruits = []
for fruit in fruits:
    reverse_fruits.append(fruit[::-1])
print("\nList containing reverse of each fruit name:")
print(reverse_fruits)