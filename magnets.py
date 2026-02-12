n = int(input())
magnets = []
for _ in range(n):
    pairs = input()
    magnets.append(pairs)
groups = 1
for i in range(len(magnets)-1):
    if magnets[i] != magnets[i+1]:
        groups += 1
print(groups)
