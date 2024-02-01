students=['ram','joy','dennis','soman']
for i in students:
    print(i)

for i in range(len(students)):
    print(i)
students=['ram','joy','dennis','soman','rose','chandler']
i=0
while (i<6):
    print(students[i])
    i=i+1
    
numbers=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=[] 
even_numbers=[] 

for i in range(len(numbers)):
    if i %2==0: 
        even_numbers.append(i)
    else:
        odd_numbers.append(i)  
print(odd_numbers)
print(even_numbers)

sub=['english','malayalam','chemistry','physics']
subject=[]
for  i in range(len(sub)):
    if 's' in sub[i]:
        subject.append(i)
print(subject)

#list comprehension
sub=['english','malayalam','chemistry','physics']
subject=[i for i in sub if 's' in i]
print(subject)

a=[1,2,3,4,5,6]


for i in range(len(a)):
    sqr=a[i]*a[i]
    cube=a[i]*a[i]*a[i]
    print('sqr is:',sqr)
    print('cube is:',cube)


elements=['abc','xyz','1221','pqr']
for i in range(len(elements)):
    if '2' in elements[i]:
        print(elements[i])


a=[1,2,3,4,5]
print(2*a)


a=[1,2,3,4,5,6,7,8,9,10]
print('largest number is:',max(a))
print('smallest number is:',min(a))
a[2]=24
print(a)







        