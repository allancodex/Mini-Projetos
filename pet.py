#practicing a bit of inheritance
class Pet:
  def __init__(self, name, age):
    self.name = name 
    self.age = age

  def show(self):
    print(f'I am {self.name} and I am {self.age} years old')


class Cat(Pet):
  def __init__(self, name, age, color):
    super().__init__(name,age) #SUPERDUPER IMPORTANT LINE TO REMEMBER
    self.color = color
    
  def speak(self):
    print('Meow')

  def show(self):
    print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):
  def speak(self):
    print('Bark')

p1 = Pet('Bob', 9)
p1.show()
c = Cat('Bill', 3, 'blue')
c.show()
d = Dog('Jill', 4)
d.show()
