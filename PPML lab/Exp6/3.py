sentence = input("Enter a sentence: ")
list1 = sentence.split()
print("\nElements of list1 with index:")
for index, word in enumerate(list1):
    print(index, ":", word)
list2 = list(range(1, len(list1) + 1))
list3 = list(zip(list1, list2))
print("\nElements of list3 (using zip):")
for item in list3:
    print(item)