y,w = map(int,input().split())
d = 6-max(y,w)+1
if d/6 == 1:
    print("1/1")
elif d/6 == 1/6:
    print("1/6")
elif d/6 == 1/3:
    print("1/3")
elif d/6 == 1/2:
    print("1/2")        
elif d/6 == 2/3:
    print("2/3")   
elif d/6 == 5/6:
    print("5/6")     
else:
    print(d,"0/6")

