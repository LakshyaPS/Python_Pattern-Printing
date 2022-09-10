num=int(input("enter the number of rows"))
for row in range(1,num+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()
for row in range(num-1
                 -1):
    for col in range(row):
            print('*',end=" ")
    print()
    
    
