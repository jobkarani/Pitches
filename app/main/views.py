from flask import render_template, redirect, url_for, abort, flash, request
from . import main
from flask_login import login_required, current_user

from app.models import User, Post, Category
# from .. import db,images
from .forms import CatForm



@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    print(posts)
    return render_template('index.html', posts=posts)



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
