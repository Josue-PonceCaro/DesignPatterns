class Person:
    def __init__(self):
        self.name = None
        self.age = None
    def __str__(self) -> str:
        return f'The name is {self.name} and the age is {self.age}'

class PersonBuilder:
    def __init__(self, person=None):
        if person == None:
            self.person = Person()
        else:
            self.person = person
        # todo
    @property
    def name(self):
        return nameBuilder(self.person)

    @property
    def age(self):
        return ageBuilder(self.person)
    def __str__(self):
        pass
    def build(self):
        return self.person

class nameBuilder(PersonBuilder):
    def __init__(self, person=None):
        super().__init__(person)
    def IS(self,name):
        self.person.name = name
        return self

class ageBuilder(PersonBuilder):
    def __init__(self, person=None):
        super().__init__(person)
    def IS(self, age):
        self.person.age = age
        return self

if __name__ == '__main__':
    p1 = PersonBuilder().name.IS('Peper').age.IS(21)

    print(type(p1))