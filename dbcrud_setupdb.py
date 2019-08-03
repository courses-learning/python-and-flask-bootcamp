from dbcrud_practice import db, Animal

db.create_all()

polar_bear = Animal('Polar Bear', 'Rex', 12)
elephant = Animal('Elephant', 'Ethel', 23)

print(polar_bear.id)
print(elephant.id)

db.session.add_all([polar_bear, elephant])

db.session.commit()

print(polar_bear.id)
print(elephant.id)
