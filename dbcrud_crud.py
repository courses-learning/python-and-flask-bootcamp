from dbcrud_practice import db, Animal

##create##
lion = Animal('Lion', 'Leo', 8)
db.session.add(lion)
db.session.commit()

polar_bear2 = Animal('Polar Bear', 'Scooby', 15)
db.session.add(polar_bear2)
db.session.commit()

##read##
all_animals = Animal.query.all()
print(all_animals)

##select by id##
animal_one = Animal.query.get(1)
print(animal_one.type)

##filters##
polarbears_list = Animal.query.filter_by(type='Polar Bear')  # produces sql code
print(polarbears_list.all())

##update##
first_animal = Animal.query.get(1)
first_animal.age = 2
db.session.add(first_animal)
db.session.commit()

##delete##
second_animal = Animal.query.get(2)
db.session.delete(second_animal)
db.session.commit()

# re-show all
all_animals = Animal.query.all()
print(all_animals)
