class ramesh:
    def __init__(self,n,a,g) :
     self.name=n
     self.age=a
     self.gender=g
    def talk(self):
       print("hi i am ",self.name)
   
    def vote(self):
     if (self.age<18):
        print("I am not eligibe to vote")
     else:
        print("i an eligiblen to vote ")

obj1=ramesh("ramesh  giri",22,"male")
obj2=ramesh('vicky kumar',17,"male")
obj1.talk()
obj1.vote()
obj2.talk()
obj2.vote()

class vicky(ramesh):
  def son(self,n,a,g):
    self.name=n
    self.age=a
    self.gender
  def rahul(self):
     print("hi my name is ",self.name)
obj3=vicky("rahul",6,"male")
obj3.rahul()


