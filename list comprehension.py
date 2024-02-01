sub=['english','malayalam','chemistry','physics']
subject=[]
for  i in sub:
    if 's' in i:
        subject.append(i)
print(subject)

#list comprehension
sub=['english','malayalam','chemistry','physics']
subject=[i for i in sub if 's' in i]
print(subject)

num=[i for i in range(11)]
print(num)

sub=['english','malayalam','chemistry','physics']
subject=[i.upper() for  i in sub]

print(subject)

num=[i for i in range(11)  if i<5]
print(num)

#sorting

a=[1,7,6,3,2,5]
a.sort()
print(a)

a=[1,7,6,3,2,5]
a.sort(reverse=True)
print(a)

list=[1,2,3,4,5,6]
list1=list.copy()
print(list1)

a=[1,3,5,7,9]
b=[2,4,6,8,0]
print(a+b)



a=['red','blue','green','black']
print(a[0])
print(a[len(a)-1])

colours=['red','blue','green','black','violet','blue']
colour=[]
for i in range(len(colours)):
    if colours[i] not in colour:
        colour.append(colours[i])
        print(colour)



a=['dog','cat','fox']
print(a)
a.clear()
print(a)



