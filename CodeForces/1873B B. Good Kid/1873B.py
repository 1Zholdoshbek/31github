t=int(input())
for j in range(t):
    summ=1
    u=int(input())
    l=[int(i) for i in input().split()]
    l.sort()
    for m in range(1,len(l),1):
        summ*=l[m]
    print(summ*(l[0]+1))