n = input()
s = input()
neighbor = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        neighbor+=1
print(neighbor)
