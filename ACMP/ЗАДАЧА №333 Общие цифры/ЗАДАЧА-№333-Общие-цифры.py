a,b,c=input().split()
sets=set()
for i in a:
    if i in b and i in c:
        sets.add(i)
l=list(sets)
l.sort()
print(len(sets))
for i in l:
    print(i,end=" ")