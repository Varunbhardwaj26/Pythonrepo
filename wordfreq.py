from collections import Counter
def wordfreq():
    word=input("Enter a word:")
    frq=Counter(word)
    for i in frq:
        print(i,":",frq[i])
wordfreq()
 