
for i in range(5):
 for j in range(i+1):
   print(i+1,end='')
 print()

for i in range(5):
  for j in range(1,i+1):
    print(j,end='') 
  print()

row=5
b=0
for i in range(5,0,-1):
  b+=1
  for j in range(1,i+1):
    print(b,end='')
  print()

for i in range(5,0,-1):
  for j in range(0,i):
    print(5,end='')
  print()

for i in range(5):
 for j in range(i+1):
    print('*',end='')
 print()

for i in range(5):
    for j in range(5-i):
        print('*',end='')
    print()
