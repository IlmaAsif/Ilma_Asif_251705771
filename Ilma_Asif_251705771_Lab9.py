class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Display(self):
        print("Name:",self.name)
        print("Age:",self.age)


class House:
    def __init__(self,address,numberofrooms):
        self.address=address
        self.nor=numberofrooms
        self.lop=[]
    def add(self,x):
        self.lop.append(x)
        
    def remove(self,y):
        self.lop.remove(y)

    def display(self):

        print("the following people are living in the house")
        for x in self.lop:
            x.Display()

    
person=Person("barbie",16)
house=House("xyx",3)
house.add(person)

house.display()