
def Check():
    n=int(input())
    if n==9 or n<7:
        print('NO')
    else:
        print("YES")
        if(n%3!=0):
            print(1," ",2," ",n-3)
        else:
            print(1," ",4," ",n-5)
 
t=int(input())
while(t):
    Check()
    t-=1