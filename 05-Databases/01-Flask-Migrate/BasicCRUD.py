from BasicModelApp import db, Puppy

############
## CREATE ##
############

my_puppy = Puppy('Rufus',5, 'Lab')
db.session.add(my_puppy)
db.session.commit()


##########
## READ ##
##########

all_puppies = Puppy.query.all()
# list of all puppies in table using the defined __repr__
print(all_puppies)
