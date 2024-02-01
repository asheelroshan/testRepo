def name():
    print('hello')
name()   

def name(x):
    print(x)
name('roshan')    

def age(y):
    print(y)
age(24)   

def age(a):
    print(a)
age(a=24)

def name(country = 'india'):
    print('i am from' +  country)
name( 'brazil')
name( 'saudi')
name()
name( 'sweden') 

def fruits(list):
    for x in list:
        print(x)
name=['apple','orange','mango','banana']
fruits(name)

#multipication table
def mul(n):
    for i in  range(1,11): 
        print(i*n)    
a=int(input('enter a number'))
mul(a)

def number(n):
 if n%2==0:
     print('it is even number')
 else:
     print('it is odd number')
b=int(input('number is'))
number(b)

#uppercase
c=input('enter a name')
def name(n):
    f=c.upper()
    print(f)
name(c)

#vowels and constants
def name(n):
    v=['a','e','i','o','u','A','E','I','O','U']
    vcount=0
    dcount=0
    for i in range(len(n)):
        if n[i] in v:
            vcount=vcount+1
        else:
            dcount=dcount+1
    print(vcount)
    print(dcount)
a=input('enter a string')
name(a)

def radius(r):
    area=3.14 *r*r
    print(area)
b=int(input('area is'))
radius(b)

def season(s):
    if s=='rainy':
        print('chappal')
    elif s=='summer':
        print('shoe')
    else :
        s=='winter'
        print('boots')
q=input('enter the season')
season(q)







