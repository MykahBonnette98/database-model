#importing from database_flask file the puppy model/table
from database_flask import db,Puppy

#creates all the tables -> db table
db.create_all()

#creating two puppy objects
sam = Puppy('Sammy',3)
frank = Puppy('Frank',4)

print(sam.id)
print(frank.id)

#adding all to database
db.session.add_all([sam,frank])

#commit changes to database
db.session.commit()

print(sam.id)
print(frank.id)


