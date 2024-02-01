fruits=('apple','orange','mango')
print(fruits)
print(len(fruits))

print(fruits[1])
print(fruits[-1])
print(fruits[:2])
print(fruits[2:])
if 'apple' in fruits:
    print('yes')
a=list(fruits) 
print(a)
a[0]='kiwi'
b=tuple(a)
print(b)
c=list(b)
print(c)
c.append('cherry')
print(c)
d=tuple(c)
print(d)
e=list(d)
print(e)
e.remove('orange')
print(e)
animal=('fox','cat','dog','tiger','lion')
(x,y,*z)=animal
print(x)
print(y)
print(z)

(x,*y)=animal
print(x)
print(y)


birds=('parrot','pigeon','eagle','duck','crow')
print(birds)
(x,y,*z)=birds
print(x)
print(y)
print(z)

birds=('parrot','pigeon','eagle','duck','crow')
print(birds)
for i in range(len(birds)):
    print(birds[i])
i=0
while(i<5):
    print(birds[i])
    i=i+1

animal=('fox','cat','dog','tiger','lion')  
birds=('parrot','pigeon','eagle','duck','crow')
c=(animal+birds)
print(c)

a=(1,2,3,4,5,3,4,3)
count=a.count(3)
print(count)

num=a.index(4)
print(num)

print(a[2:5])




