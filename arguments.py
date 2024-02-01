#arbitrary arguments

def myfunction(*kids):
    print("the smallest kid is " +kids[2])
myfunction("manu","sonu","vinu")

#keywords arguments

def myfunction(kid1,kid2,kid3):
    print("the smallest kid is "+kid1)
myfunction(kid1="manu",kid2="sonu",kid3="vinu")

#keywords arbitrary arguments

def myfunction(**kid):
    print("the little kid is " +kid["kid1"])
myfunction(kid2="manu",kid1="sonu")

#default parameter

def myfunction(country="saudi"):
    print("i am from" +country)
myfunction("sweden")
myfunction()
myfunction("india")

#list

def myfunction(fruits):
    for n in fruits:
        print(n)
food=["apple","orange","mango"]
myfunction(food)

#return

def myfunction(fruits):
    return(fruits +2)

print(myfunction(1))

#try,except,else,finally

try:
    print('x')
except:
    print("error occured")
else:
    print("ok")

try:
    print('x')
except:
    print("error occured")
finally:
    print("okay")









