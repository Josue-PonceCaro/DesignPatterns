# class CodeBuilder:
#     def __init__(self, root_name):
#         # todo

#     def add_field(self, type, name):
#         # todo

#     def __str__(self):
#         # todo

class Person:
    def __init__(self):
        self.name = None
        self.age = None
    

class CodeBuilder:
    def __init__(self, person):
        if person == 'Person':
            self.person = Person()
   
    def add_field(self, type, name):
        if type == 'name':
            self.person.name = name
            return self
        elif type == 'age':
            self.person.age = int(name)
            return self.person



cb = CodeBuilder('Person').add_field('name','""').add_field('age','0')
print(cb)


