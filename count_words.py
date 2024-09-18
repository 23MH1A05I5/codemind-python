def count(words):
    vowels="aeiouAEIOU"
    c=0
    for i in words:
        if (i[0] in vowels)  and (i[-1] not in vowels):
            c+=1
    return c      
n=input().split()
print(count(n))
