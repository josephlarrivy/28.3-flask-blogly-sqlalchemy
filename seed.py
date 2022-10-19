from models import User, db, Post
from app import app

# create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()

# add starter data

person1 = User(first_name='John', last_name='Doe', image_url = 'www.google.com')

person2 = User(first_name='Jane', last_name='Doe', image_url='www.google.com')

person3 = User(first_name='Jim', last_name='Doe', image_url='www.google.com')

post1 = Post(title="post1", content="post1 content", user_id="1")

# Add new objects to session, so they'll persist
db.session.add(person1)
db.session.add(person2)
db.session.add(person3)
# Commit
db.session.commit()
# Add new objects to session, so they'll persist
db.session.add(post1)
# Commit
db.session.commit()
