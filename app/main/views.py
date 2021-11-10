from flask import render_template, redirect, url_for, abort, flash, request
from . import main
from flask_login import login_required, current_user

from app.models import User, Post, Category
# from .. import db,images
from .forms import UpdateProfile,CommentsForm,PostForm



@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    print(posts)
    return render_template('index.html', posts=posts)
@main.route('/posts')
def posts():
    posts = Post.query.all()
    # sales = Post.query.filter_by(category = 'sales').all() 
    # interview = Post.query.filter_by(category = 'interview').all()
    # elevator = Post.query.filter_by(category = 'elevator').all()
    # promotion = Post.query.filter_by(category = 'promotion').all()
    # personal = Post.query.filter_by(category = 'personal').all()
    # pickuplines = Post.query.filter_by(category = 'pickuplines').all()

    title = 'PitchDom -  Welcome to PitchDom'
    return render_template('posts.html', title=title , posts = posts )
@main.route('/addpost',methods = ['GET', 'POST'])
@login_required
def addposts():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Post(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.post'))
        

        return(redirect(url_for('main.category')))
    title = 'Add-Post -  Welcome to PitchDom'
    return render_template('addpost.html', title=title, post_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/add_category', methods=['GET', 'POST'])
def add_cat():
    form = CatForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('Category added successfully.')
        return redirect(url_for('.index'))
    return render_template('add_category.html', form=form)
