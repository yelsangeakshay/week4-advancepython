import pickle

class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    
    def show_attribute(self):
        return self.name,self.age

p = Person("Akshay","29")

with open("person.pkl",'wb') as f:
    pickle.dump(p,f)

with open("person.pkl",'rb') as f:
    p = pickle.load(f)
print("Person Attributes",p.show_attribute())