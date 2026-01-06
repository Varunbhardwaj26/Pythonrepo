from collections import Counter
def wordfreq(st):
    word=st.lower().split()
    count1=Counter(word)
    for i in count1:
        print(i,":",count1[i])
wordfreq("I am a student of a college student")