from flask import render_template, url_for, flash, redirect, request
from backend import app, db, bcrypt
from backend.forms import RegistrationForm, LoginForm, LostItemForm, PostForm
from backend.models import User, LostAndFound, ForumPost
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('main_page.html')

@app.route("/lost_and_found")
def lost_and_found():
    items = LostAndFound.query.all()
    return render_template('lost_and_found.html', items=items)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/report_lost", methods=['GET', 'POST'])
@login_required
def report_lost():
    form = LostItemForm()
    if form.validate_on_submit():
        item = LostAndFound(item_name=form.item_name.data, description=form.description.data, author=current_user)
        db.session.add(item)
        db.session.commit()
        flash('Your lost item report has been submitted!', 'success')
        return redirect(url_for('lost_and_found'))
    return render_template('report_lost.html', title='Report Lost Item', form=form)

@app.route("/forum", methods=['GET', 'POST'])
@login_required
def forum():
    form = PostForm()
    if form.validate_on_submit():
        post = ForumPost(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('forum'))
    posts = ForumPost.query.all()
    return render_template('forum.html', title='Forum', form=form, posts=posts)

@app.route("/resources")
@login_required
def resources():
    return render_template('resources.html')
