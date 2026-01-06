from collections import Counter
def isanagram():
    word1=input("Enter word1:").lower()
    word2=input("Enter word2:").lower()
    return Counter(word1)==Counter(word2)

print(isanagram())