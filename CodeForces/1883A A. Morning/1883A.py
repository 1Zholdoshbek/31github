t=int(input())
for i in range(t):
    cnt=0
    x=int(input())
    a=int(x/1000)%10
    b=int(x/100)%10
    c=int(x/10)%10
    d=x%10
    if a==0:
        a=10 
    if b==0:
        b=10 
    if c==0:
        c=10 
    if d==0:
        d=10 
    cnt=a+abs(b-a)+1+abs(c-b)+1+abs(d-c)+1
    print(cnt)