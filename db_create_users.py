from routes import db
from models import User

# insert data
db.session.add(User("admin", "admin", "ad@min.com", "P@ssw0rd!"))
db.session.add(User("Nupur", "Patel", "npatel@fcsinet.com", "let-me-in"))

# commit the changes
db.session.commit()