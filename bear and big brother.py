lamik,bob = map(int,input().split())

year = 0
while lamik <= bob:
    year+=1
    lamik*=3
    bob*=2
print(year)
