from collections import Counter

n = input()
s = input()
s = Counter(s)
if s['D'] == s["A"]:
    print("Friendship")
elif s['A'] > s['D']:
    print("Anton")
else:
    print("Danik")
