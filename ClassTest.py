class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self,str):
        print('我是人',str)
# Man为Person的子类
class Man(Person):
     def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex
     def __str__(self,str):
        print('我是男人',str)


person = Person('jack', 12)
man = Man('jack', 20, '男')
# print(person.name.title(), person.age)
print(man.name.title(), man.age,man.sex,man.__str__(man.name))
