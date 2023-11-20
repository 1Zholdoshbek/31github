def mysort(s1,s2):
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    return l1==l2
def mycheck(s1,s2):
    for i in range(0,len(s1),1):
        if s1[i]==s2[i]:
            return False
    return True
s1,s2=input().split()
if(mycheck(s1,s2) and mysort(s1,s2)):
    print('YES')
else:
    print('NO')