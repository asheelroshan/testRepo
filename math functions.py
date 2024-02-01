x=min(1,2,3)
y=max(4,5,6)
print(x)
print(y)

x=abs(-5.9)
print(x)

y=pow(3,4)
print(y)

import math
x=math.sqrt(144)
print(x)

import math
x=math.pi
print(x)

import datetime
y=datetime.datetime.now()
print(y)

import datetime
z=datetime.datetime(2000,4,11)
print(z.strftime("%B"))
print(z.strftime("%a"))

#string format

age=23
txt="my name is asheel and i am {}"
print(txt.format(age))

#i want 3 pieces of item 567 for 49.95 dollars
pieces=3
item=567
dollars=49.95
txt="i want {} pieces of item {} for {} dollars"
print(txt.format(pieces,item,dollars))

#i want to pay 49.95 dollars for 3 pieces of item 567
pieces=3
item=567
dollars=49.95
txt="i want to pay {2} dollars for {0} pieces of item {1} "
print(txt.format(pieces,item,dollars))

#area of circle sqrt 1250,356,121,525,169
#min value from 80,83,61,84,21,19,89,20,max
#ceil,floor          2.8,3.1,2.5

import math
r=int(input('enter a number'))
y=math.pi
area=y*r*r
print(area)

x=math.sqrt(1250)
print(x)
x=math.sqrt(356)
print(x)
x=math.sqrt(121)
print(x)
x=math.sqrt(525)
print(x)
x=math.sqrt(169)
print(x)

x=min(80,83,61,84,21,19,89,20)
print(x)

x=max(80,83,61,84,21,19,89,20)
print(x)

y=math.ceil(2.5)
print(y)
z=math.floor(3.9)
print(z)

age=23
year=2005
date=11
txt="my sister was of age {} in the year {} and the date was {} "
print(txt.format(age,year,date))

age=23
year=2005
date=11
txt="the date was {2} in the year {1} when my sister was of age {0}"
print(txt.format(age,year,date))


