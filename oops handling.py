class car():
   
#init method or constuctor
  def __init__(self,model,color):
    self.model=model
    self.color=color

  def view(self):
     print("model is",self.model)
     print("color is",self.color)

audi=car("audi a4","blue")
benz=car("benz gwagon","black")

audi.view()
benz.view()

print("the model is",audi.model)

class person(object):
     def __init__(self,name):
        self.name=name
     def getName(self):
        return self.name
     def isEmployee(self):
        return False
class Employee(person):
     def isEmployee(self):
        return True
x=person("name1")
print(x.getName(),x.isEmployee())
x=Employee("name2")
print(x.getName(),x.isEmployee())







    