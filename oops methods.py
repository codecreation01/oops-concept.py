#stores the employee details in the form of list 
#gives information about employee name,age,designation,year of joining
kirk=["james kirk",34,"captain",2265]
spock=["spock",35,"science officer",2254]
mccoy=["leocordmccoy",30,"chief medical officer",2266]

#class is being created
class dog:
  pass

#init() method is being created in the class
#the method creates name and age attributes
class dog:
  def_init_(self,name,age)
  
  
#class attribute is created
#class attribute  is given the value canis familiaris
class dog:
  species="canis familiaries"
  def_init_(self,name,age)
  
  
#two objects are being created 
#objects are being compared and result is in boolean value
class dog:
  dog()
  dog()
  a=dog()
  b=dog()
  a==b
  
#object instance is specific realization of any object
#object instance is being created
buddy=dog.("buddy",9)
miles=dog.("miles",10)

#demonstartes the accessing of class attributes
#returns the species value
buddy.species

#demonstartes that the values are mutable
buddy.age=10
miles.species="felis silverstris"


#instantance methods are functions within class
#instance methods are created

class dog:
  species="canies familiaries"
  
  def_init_(self,name,age):
    self.name=name
    self.age=age
    
  def description(self):
    return "{self.name} is {self.age} years old"
  def speak(self.sound):
    return "{self.name} says {sound}"
  
#type method determines which class an object belong to
#returns the type of the class

miles=jackrusselTerrior("miles",4)
type(miles)

#this method determines wether the it is instance of a class
#returns a boolean value

isinstance(miles,dog)

#demonstartes method overridding
#parent class method has been used in child class

class jackrusselterrior(dog):
  def speak(self,sound="arf"):
    return{self.name} says {sound}"
  miles=jackrusselterrior("miles",4)
  miles.speak()
  
#demonstarates the working of superkeyword
#parent class can be accessed from within a method of child class using super()

class jackrusselterrior(dog):
  def speak(self,sound="arf"):
    return super().speak(sound)




