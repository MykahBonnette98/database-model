from database_flask import db, Puppy

##create
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

#read
all_puppies = Puppy.query.all() #list of puppies in table
print(all_puppies)

#select by id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#filters
puppy_frank = Puppy.query.fiter_by(name='frank')
print(puppy_frank.all())

#result from ^
# ['frank is 3 years old']

#update
first_puppy = Puppy.query.get(1)
db.session.add(first_puppy)
db.session.commit()

#deleting
second_pup = Puppy.query(2)
db.session.delete(second_pup)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)