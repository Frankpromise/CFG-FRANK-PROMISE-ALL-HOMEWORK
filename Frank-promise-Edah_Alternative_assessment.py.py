#TASK1

from datetime import datetime
from dateutil.relativedelta import relativedelta

class Animal:

    def __init__(self, name, dob, colour, owner):
        self.name = name
        self.dob: datetime = dob
        self.colour = colour
        self.owner = owner

    @property
    def delta(self):
        return relativedelta(datetime.now(), self.dob)

    @property
    def years(self):
        return self.delta.years

    @property
    def months(self):
        return self.delta.months

    def get_age(self):
        # you may need to import some packages to manipulate dates
        return {'years': self.years, 'months': self.months}
# B.1

class Dog(Animal):
    def __init__(self, name, dob, colour, owner, pet_id, breed):
        super().__init__(name, dob, colour, owner)
        self.pet_id = pet_id
        self.breed = breed

    @staticmethod
    def sound():
        return 'Woof!'

# B.2
class Cat(Animal):
    def __init__(self, name, dob, colour, owner, pet_id, breed):
        super().__init__(name, dob, colour, owner)
        self.pet_id = pet_id
        self.breed = breed

    @staticmethod
    def sound():
        return 'Meow'

# C
class PetOwner:
    def __init__(self, name, pet_id):
        self.name = name
        self.pet_id = pet_id

#  TASK2 
pet_info = [
    {'breed': 'German Shepherd',
     'colour': 'brown',
     'dob': '2021/09/21',
     'pet_id': 10025,
     'name': 'Lola',
     'owner': 'Maria Smith',
     'type': 'dog'},
    {'breed': 'Blue Russian',
     'colour': 'white',
     'dob': '2010/03/06',
     'pet_id': 10058,
     'name': 'Snowy',
     'owner': 'Malcolm Graham',
     'type': 'cat'},
    {'breed': 'Border Collie',
     'colour': 'beige',
     'dob': '2019/11/18',
     'pet_id': 10042,
     'name': 'Bailey',
     'owner': 'Priya Patel',
     'type': 'dog'},
    {'breed': 'Pug',
     'colour': 'black',
     'dob': '2021/10/16',
     'pet_id': 10053,
     'name': 'Ziggy',
     'owner': 'Mohamed Moussa',
     'type': 'dog'},
    {'breed': 'Sphynx',
     'colour': 'white',
     'dob': '2015/08/23',
     'pet_id': 10026,
     'name': 'Coco',
     'owner': 'Jennifer Coley',
     'type': 'cat'}
]


def get_animal_class(type: str):
    if type == 'dog':
        return Dog

    if type == 'cat':
        return Cat

    raise Exception('class not found')


def register_pets(data: list):
    pets = {}

    for pet in data:
        #   convert DOB to datatime object and reassign to its key
        dob_datetime = datetime.strptime(pet["dob"], '%Y/%m/%d')
        pet["dob"] = dob_datetime

        # initialize the pet Owner as a class and reassign it to its Key
        pet["owner"] = PetOwner(pet["owner"], pet["pet_id"])

        #   create animal instance
        animal_class = get_animal_class(pet["type"])
        del pet["type"]
        animal = animal_class(**pet)

        pets[pet["pet_id"]] = animal

    return pets


print(register_pets(pet_info))


# TASK3 


# using recursion
def sum_of_digits(n):
    if n == 0:
        return n
    else:
        return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(333)) #9
print(sum_of_digits(12345))  #15
print(sum_of_digits(78)) #15


# TASK4



"""
The example violates the Liskov Substitution of the SOLID principles. 
LSP states that objects of a parent class can be replaceable with objects of its child 
classes without breaking the app. For that to be feasible, it requires the child classes to behave in 
same way as the objects of the parent class. 
In the example, the square class is not complying with the behaviour of the rectangle. 
It's overriding the height/width of the parent class, and this can lead to maintenance and testing problems.
If someone writes separate unit tests to calculate the area of the rectangle and the square, they will probably pass.
But if they try to find the area of the rectangle using the object of square, it might fail. 
A possible solution to this situation would be to let each shape have its own data including defining 
its own area method. So rather than square inheriting from rectangle, you could create a common base class and
have both shapes inherit that instead. 
"""
