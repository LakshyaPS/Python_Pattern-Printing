num=int(input("Enter The Number Of Rows That You Want In Your Fibonacci Series:"))
first=0
second=1
for row in range(1,num+1):
    print(first)
    temp=first
    first=second
    second=temp+first
