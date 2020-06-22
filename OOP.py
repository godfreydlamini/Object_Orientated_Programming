 
class Person:
    def __init__(self,name,age,gender,interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests
    def hello(self):
        print("Hello My name is" + " " + self.name + " "+"and i am "+" "+ self.age +""+"years old my interests are"+" "+self.interests)

person = Person("Godfrey", "27", "male", "carpentry work, football and business.")
person.hello()