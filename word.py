word = input()
ups = 0
lowers = 0
for char in word:
    if char.isupper():
        ups+=1
    else:
        lowers+=1
if ups > lowers:
    print(word.upper())
else:    
    print(word.lower())
