# class Person:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

# class PersonFactory:
#     def create_person(self, name):
#         # todo
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    count = -1
    def create_person(self, name):
        PersonFactory.count +=1
        return Person(PersonFactory.count, name)

a = PersonFactory()
p1 = a.create_person('pepe')
p2 = a.create_person('lucho')

print(p1.id)
print(p2.id)