s=input()
l=s[::-1]
sets=set(s)
if(len(sets)==1):
    print('NO SOLUTION')
elif(len(s)==(len(sets))):
    print(s)
elif s==l:
    print(s[:len(s)-1])
else:
    print(s)