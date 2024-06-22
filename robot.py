class Robot:
  def __init__(self, name, color, weight):
    self.name = name
    self.color = color
    self.weight = weight

  def introduce_self(self):
    print(f"Hello there, my name is {self.name}")

r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry','blue',40)
#r1.introduce_self()
#r2.introduce_self()

class Person:
  def __init__(self, name, personality, isSitting, robot_owned):
    self.name = name
    self.personality = personality
    self.isSitting = isSitting
    self.robot_owned = robot_owned
    
  def sit_down(self):
    self.isSitting = True

  def stand_up(self):
    self.isSitting = False

  def relationships(self):
    print(f'Hello, my name is {self.name} i am a {self.personality} person and my robot is {self.robot_owned.name}')  

p1 = Person('Alice', 'aggressive', False, r1)
p2 = Person('Becky', 'talkative', True, r2)

p1.relationships()
p2.relationships()




