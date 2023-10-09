from typing import Counter


def frequencySort( s):
    dict= Counter(s)
 
    si=sorted(dict,reverse=True,key=lambda x:dict[x])
    newArr=[]
    for i in si:      
        newArr=newArr+[i*dict[i]]


    return "".join(newArr)




s = "eert"
print(frequencySort(s))
    