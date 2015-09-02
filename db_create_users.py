from models import db, User
import os

# create the database and the db table
#db.init_app(app)
db.create_all()

# insert data
db.session.add(User("admin", "admin", "ad@min.com", "P@ssw0rd!"))
db.session.add(User("Nupur", "Patel", "npatel@fcsinet.com", "let-me-in"))

# commit the changes
db.session.commit()