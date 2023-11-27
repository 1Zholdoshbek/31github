t=int(input())
tmp="Yes"*50
for i in range(t):
    s=input()
    if s in tmp:
        print("YES")
    else:
        print("NO")