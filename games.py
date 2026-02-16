home=[]
away = []
ans = 0
for _ in range(int(input())):
    h,a = map(int,input().split())
    home.append(h)
    away.append(a)
for i in home:
    for j in away:
        if i == j :
            ans+=1
print(ans)
