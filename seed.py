from models import City, db
from app import app

# create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
City.query.delete()

# add starter data to cities

Albertville = City(name="Albertville", country="United States", state_province="Minnesota", population=7281)

Alexandria = City(name="Alexandria", country="United States", state_province="Minnesota", population=11680)

Anoka = City(name="Anoka", country="United States", state_province="Minnesota", population=17276)

Austin = City(name="Austin", country="United States", state_province="Minnesota", population=24716)

# Add new objects to session, so they'll persist
db.session.add(Albertville)
db.session.add(Alexandria)
db.session.add(Anoka)
db.session.add(Austin)

# Commit
db.session.commit()
