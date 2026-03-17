para = "noon time is good"
para_lower = para.lower()
words = para_lower.split()
word_count = 0
for w in words:
    word_count += 1
palindrome_count = 0
for word in words:
    rev = ""
    for ch in word:       
        rev = ch + rev
    if word == rev:
        palindrome_count += 1
print("Each word in reverse order:")
for word in words:
    rev_word = ""
    for ch in word:        
        rev_word = ch + rev_word
    print(rev_word)
print("\nTotal number of words:", word_count)
print("Total number of palindromes:", palindrome_count)