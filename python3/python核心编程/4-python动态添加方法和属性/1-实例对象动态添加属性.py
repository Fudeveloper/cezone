from Person import Person

p1 = Person('wang',30)
# print(p1.gender)      # AttributeError: 'Person' object has no attribute 'gender'
p1.gender = 'Male'
print(p1.gender)        #Male