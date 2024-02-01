import math
c=5
print(math.factorial(c))


import datetime
now=datetime.datetime.now()
print(now)
year=lambda x:x.year
month=lambda x:x.month
day=lambda x:x.day
time=lambda x:x.time()
print(year(now))
print(month(now))
print(day(now))
print(time(now))


student=[ {'price':200,
        'colour':'red'},
             
     {'price':150,
         'colour':'orange'},

     {'price':120,
        'colour':'purple'},
     ]
student.sort(key=lambda a:a['price'])
print(student)



             


    