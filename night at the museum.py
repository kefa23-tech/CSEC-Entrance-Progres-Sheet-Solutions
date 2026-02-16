s = input()
s = [ord(i) for i in s]
dist = 0
diff = abs(ord("a") - s[0])
dist+=min(diff,26-diff)
for i in range(len(s)-1):
    diff= abs(s[i]-s[i+1])
    dist+=min(diff,26-diff)
print(dist)
