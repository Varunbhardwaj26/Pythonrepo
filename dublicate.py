from collections import Counter

def isdublicate(l1):
    dub=Counter(l1)
    for i in dub:
        if dub[i]>1:
            print(i,":",dub[i])
    # dub=[]
    # for i in l1:
    #     if i in dub:
    #         print("Dublicate num:",i)
    #     else:
    #         dub.append(i)

isdublicate([1,2,4,5,2,3,1,7,1]) 
