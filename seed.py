from models import db, User, Post, PostTag, Tag
from app import app

# create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()
PostTag.query.delete()
Tag.query.delete()

# add starter data

person1 = User(first_name='John', last_name='Doe', image_url = 'www.google.com')
person2 = User(first_name='Jane', last_name='Doe', image_url='www.google.com')
person3 = User(first_name='Jim', last_name='Doe', image_url='www.google.com')

post1 = Post(title="post1", content="post1 content", user_id=1)
post2 = Post(title="post2", content="post2 content", user_id=2)
post3 = Post(title="post3", content="post3 content", user_id=3)

tag1 = Tag(name='tag1')
tag2 = Tag(name='tag2')
tag3 = Tag(name='tag3')

posttag1 = PostTag(post_id=1, tag_id=1)
posttag2 = PostTag(post_id=2, tag_id=2)
posttag3 = PostTag(post_id=3, tag_id=3)


# Add people to session
db.session.add(person1)
db.session.add(person2)
db.session.add(person3)
db.session.commit()
# Add posts to session
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.commit()
# Add tags to session
db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)
db.session.commit()
# Add posttags to session
db.session.add(posttag1)
db.session.add(posttag2)
db.session.add(posttag3)
db.session.commit()
