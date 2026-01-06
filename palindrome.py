def palindrome():
    word=input("Enter a word:").lower()
    return word==word[::-1]
print(palindrome())
