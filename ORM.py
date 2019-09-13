from peewee import SqliteDatabase, Model, CharField, DateField, BooleanField, ForeignKeyField
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    date_of_birth = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Pet(Model):
    name = CharField()
    owner = ForeignKeyField(Person, related_name='pets')
    animal_type = CharField()

    class Meta:
        database = db

Person.create_table()
Pet.create_table()

# uncle_bob = Person(name = 'Bob', date_of_birth = date(1961, 4, 12), is_relative = True)
# uncle_bob.save()
#
# Person.create(name = 'Jim', date_of_birth = date(1970, 1, 1), is_relative = True)

# bob = Person.select().where(Person.name == 'Bob').get() #вернет одного
# bob = Person.select().where(Person.name == 'Bob')
# bobs = list(bob)
# print(bobs)
#
# bob = bobs[0]
# bob.name = 'Bobby'
# bob.save()

jims = Person.select().where(Person.name == 'Jim')
jim = jims[0]
# Pet.create(name='Lucy', animal_type='cat', owner=jim)

cats = list(jim.pets)
print(cats[0].name)

# cats[0].delete_instance()