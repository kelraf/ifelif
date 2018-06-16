class Person():

    #INSTANCE ATTRIBUTES
    def __init__(self, name, age, gender, language):
        self.name = name
        self.age = age
        self.gender = gender
        self.language = language

    #INSTANCE METHOD 1
    def guide(self):
        return "My name is {} am {} years old. Am a {} and am doing {}.".format(self.name, self.age, self.gender, self.language)

    #INSTANCE METHOD 2
    def talk(self, sound):
        return "{} says {} {} years old.".format(self.name, sound, self.age) 

#instantiating
Object1 = Person("Rafael", 20, "Male", "Python") 
Object2 = Person("Kingwa", 23, "Male", "PHP")       

#INSTANCE class
class Person2(Person):

    #CLASS 2 METHODS
    def guide2(self):
        return "My name is {} and am {} years old.".format(self.name, self.age)

#instantiating 
Object3 = Person2("Kelvin", 20, "Male", "Python")
Object4 = Person2("Maji Moto", 20, 'Male', "java")
Object5 = Person2("Malala", 24, "Male", "Ruby") 

print(Object1.guide())
print(Object3.guide())
print(Object5.guide2())
print(Object4.talk("I am"))
