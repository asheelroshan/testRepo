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

def prime(num):
    if num==1:
        print('not prime')
    elif num>1:
        for i in range(2,num):
            if (num %i)==0:
                 print('number is not prime')
                 break
        else:
                 print('it is prime number')
    else:
        print('is not prime')
a=int(input('the number is'))
prime(a)

set={'asheel','roshan','suhail','siyad'}
print(set)

def sum(n):
        total=0
        for i in n:
         total=total+i
         print(total)
list=[1,2,3,4]
sum(list)

#lambda function
x=lambda a:a+5
print(x(5))

y=lambda a,b:a+b
print(y(5,6))

z=lambda a:a*a
print(z(2))

def square(a):
    square=a*a
    print(square)
b=int(input('square is'))
square(b)

def swap(a,b):
    a=a+b
   #  print(a)
    b=a-b
   # print(b)
    a=a-b
    print(a,b)
a=int(input('the a is ='))
b=int(input('the b is ='))
swap(a,b)

def pallindrome(a):
    if (a==a[::-1]):
         print('is pallindrome')
    else:
         print('not pallindrome')
b=input('is')
pallindrome(b)

def name(n):
    lcount=0
    hcount=0
    for i in n:
        if (i.islower()):
            lcount+=1
        elif (i.isupper()):
            hcount+=1
            
        else:
            pass
    print(lcount)
    print(hcount)
a=input('enter a string')
name(a)


b=lambda a:a+15
print(b(15))

c=lambda  a,d:a*d
print(c(4,6))










             








