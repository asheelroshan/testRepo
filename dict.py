student={
    'name':'asheel',
     'age':23,
     'place':'malappuram'
}
print(student)
print(student['age'])
print(len(student))
stud=dict(name='aa',age=22,place='hjk')
print(stud)
print(type(stud))

x=student.get('age')
print(x)

print(student.keys())
print(student.values())
print(student.items())
if 'age' in student:
    print('yes')
student['age']=55
print(student)

student.update({'place':'calicut'})
print(student)


birds={
    'name':'parrot',
    'colour':'green',
    'price':200
}

print(birds)
print(birds.keys())
print(birds.values())
print(birds.items())

students={
    'name':'asheel',
    'place':'calicut',
    'age':23
}
students.pop('age')
print(students)
students.popitem()
print(students)
stud=students.copy()
print(stud)
students.clear()
print(students)
del students
#print(students)

student={
    'apple':{'price':200,
             'colour':'red'},
             
     'orange':{'price':150,
               'colour':'orange'},

     'grapes':{'price':120,
             'colour':'purple'},
     }
print(student) 

students={
    'id1':{
        'name':'sara',
        'class':5,
        'subject':'maths,science,social'
    },

    'id2':{
        'name':'surya',
        'class':5,
        'subject':'maths,science,social'
    },

     'id3':{
        'name':'sara',
        'class':5,
        'subject':'maths,science,social'
    },

     'id4':{
        'name':'surya',
        'class':5,
        'subject':'maths,science,social'
    },
}
stud={} 
for key, value in students.items():
    if value not in stud.values():
        stud[key]=value
        print(stud)


