n=int(input())
for i in range(n):
    s=input()
    s_per="codeforces"
    cnt=0
    for i in range(len(s)):
        if s[i]!=s_per[i]:
            cnt+=1
    print(cnt)