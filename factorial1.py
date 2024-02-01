def fact(n):
    if n<0: 
      print('error')
    elif n==1 or n==0:
        print('factorial is 1')
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
    print(fact)
a= int(input('factorial is'))
fact(a)









