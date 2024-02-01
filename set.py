animals={'cat','dog','fox'}
print(animals)
print(len(animals))
print(type(animals))
birds={'parrot','pigeon','cat'}
bird=set(birds)
print(bird)
for i in animals: print(i)
animals.add('tiger')
print(animals)
animals.update(birds)
print(animals)
animals.remove('cat')
print(animals)
animals.discard('fox')
print(animals)
animals={'cat','dog','fox'}
birds={'parrot','pigeon','cat'}
i=animals.union(birds)
print(i)
j=animals.intersection(birds)
print(j)
animals.intersection_update(birds)
print(animals)
animals.difference_update(birds)
print(animals)
fruits={'apple','orange','mango'}
veg={'carrot','cucumber','orange'}
fruits.difference_update(veg)
print(fruits)
a={1,2,3,4,5,6,7,8,9,10}
b={5,6,7,1}
c=a.issubset(b)
print(c)
d=b.issubset(a)
print(d)
e=a.issuperset(b)
print(e)
f={6,8,9,4,1,0}
print(min(f))
print(max(f))
k={1,2,3,4,5,6,7}
if 8 not in k:
    print ('yes')
else:
    print('no')


a=int(input('enter a number:'))
b=int(input('enter another number:'))

op=input('Enter the operator:\n')

if op=='+':
    c=a+b
    print(c)
elif op=='-':
    c=a-b
    print(c)
elif op=='*':
    c=a*b
    print(c)
elif op=='/':
    c=a/b
    print(c)
else:
    print('not applicable!')  

animals={'cat','dog','cat','fox'}
animals.add('lion')
print(animals)

v=frozenset(animals)
print(v)

a='this is kotha raju'
v=a.partition('kotha')
print(v)

w=a.startswith('are')
print(w)

s={a,b,c}
t={a,b}
s>=t
print(s>=t)

subject=[('english',88),('maths',45),('science',90),('malayalam',87)]
subject.sort(key=lambda x:x[1])
print(subject)

b='p am asheel roshan'
c=lambda x:True if x.startswith ('p') else False
print(c(b))
