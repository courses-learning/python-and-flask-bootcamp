from db_rel_models import db, Animal, Food, Sponser

rex = Animal('Polar Bear', 'Rex')
rory = Animal('Rhino', 'Rory')

# add animals to db
db.session.add_all([rex, rory])
db.session.commit()

# check commit to db
print(Animal.query.all())

rex = Animal.query.filter_by(name='Rex').first()  # return first not a list
print(rex)

# create sponser object
david = Sponser('David', rex.id)

# assign rex some food
fish = Food('Fish', rex.id)
seal_meat = Food('Seal Meat', rex.id)

db.session.add_all([david, fish, seal_meat])
db.session.commit()

# re-check rex's entry
rex = Animal.query.filter_by(name='Rex').first()
print(rex)
rex.report_foods()
