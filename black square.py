a1,a2,a3,a4 = map(int,input().split())
s = input()
s = [int(i) for i in s]
ans = 0
for i in s:
    if i == 1:
        ans+=a1
    elif i == 2:
        ans+=a2
    elif i == 3:
        ans+=a3         
    else:
        ans+=a4
print(ans)
