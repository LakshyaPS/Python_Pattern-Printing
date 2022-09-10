string="ABCDE"
length=len(string)
for row in range (length):
  for col in range (length-row):
    print(end=" ")
  for col in range (row+1):
    print(string[row],end=" ")
  print()
