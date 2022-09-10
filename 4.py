num=5
for row in range(num,0,-1):
    for col in range(0,row-num):
        print(end=' ')
    for col in range(0,row):
        print("*",end='')
    print()
    
