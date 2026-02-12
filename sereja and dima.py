n = input()
a = list(map(int,input().split()))
sereja = 0
dima = 0
while a:
    num =max(a[0],a[-1])
    sereja+=num
    a.remove(num)

    if a:
        num =max(a[0],a[-1])
        dima+=num
        a.remove(num)
print(sereja,dima)
