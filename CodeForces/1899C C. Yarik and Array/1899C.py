n=int(input())
for i in range(n):
    k=int(input())
    a=[int(i) for i in input().split()]
    tmp=0
    min_inf=float('-inf')
    for i in range(0,len(a),1):
        if i>0 and abs(a[i]%2)==abs(a[i-1]%2):
            tmp=a[i]
            min_inf=max(tmp,min_inf)
        else:
            tmp=max(a[i],tmp+a[i])
            min_inf=max(tmp,min_inf)
    print(min_inf)