from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import Post, db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "fgh6j54ed9soikjf"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def root():
    return redirect('/list')

@app.route('/list')
def list_users():
    users = User.query.all()
    posts = Post.query.all()
    return render_template('list.html', users=users, posts=posts)

@app.route('/new_user', methods=['GET'])
def add_user_form():
    return render_template('/new_user.html')

@app.route('/new_user', methods=['POST'])
def add_user():
    new_user = User (
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        image_url = request.form['image_url'] or None
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect('/list')

@app.route('/<int:user_id>')
def users_show(user_id):
    user = User.query.get_or_404(user_id)
    posts = Post.query.all()
    return render_template('/show.html', user=user, posts=posts)

@app.route('/<int:user_id>/delete', methods=["GET","POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/list')

@app.route('/<int:user_id>/edit')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('/edit.html', user=user)

@app.route('/<int:user_id>/edit', methods=['POST'])
def edit_user_save(user_id):
    user = User.query.get_or_404(user_id)

    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']
    db.session.add(user)
    db.session.commit()

    return redirect('/list')

@app.route('/<int:user_id>/post_form')
def show_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('post_form.html', user=user)


@app.route('/<int:user_id>/post_form', methods=['POST'])
def commit_post(user_id):
    user = User.query.get_or_404(user_id)

    new_post = Post(
        title=request.form['post_title'],
        content=request.form['post_content'],
        user_id=user_id
    )
    db.session.add(new_post)
    db.session.commit()
    
    posts = Post.query.all()
    return render_template('/show.html', user=user, posts=posts)

@app.route('/<int:post_id>/post_detail_page')
def show_post_details(post_id):

    post = Post.query.get_or_404(post_id)
    return render_template('/post_detail_page.html', post=post)


@app.route('/<int:post_id>/delete_post', methods=["GET", "POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect('/list')





@app.route('/<int:post_id>/edit_post', methods=["GET"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('/edit_post.html', post=post)


@app.route('/<int:post_id>/edit_post', methods=["POST"])
def edit_post_save(post_id):
    post = Post.query.get_or_404(post_id)

    post.title = request.form['post_title']
    post.content = request.form['post_content']
    db.session.add(post)
    db.session.commit()

    return render_template('/post_detail_page.html', post=post)







# @app.route('/<int:user_id>/edit')
# def edit_user(user_id):
#     user = User.query.get_or_404(user_id)
#     return render_template('/edit.html', user=user)


# @app.route('/<int:user_id>/edit', methods=['POST'])
# def edit_user_save(user_id):
#     user = User.query.get_or_404(user_id)

#     user.first_name = request.form['first_name']
#     user.last_name = request.form['last_name']
#     user.image_url = request.form['image_url']
#     db.session.add(user)
#     db.session.commit()

#     return redirect('/list')
