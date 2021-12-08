from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, SearchForm
from app.models import User, User2Shop, UserMixin
from config import Config
from yelpapi import YelpAPI

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    title = 'Blend & Filter'
    form = SearchForm()
    if form.validate_on_submit():
        city = form.city.data
        state = form.city.data
        location = city + ", " + state
        yelp_api = YelpAPI(
                "jgAIlOyDcteIC-QzduVUg5N-PgCgKcM5_Oi2F_gp0KYCE5xSwxGftWhWdby7QTMsJ0ihq9EVXqxP7zS7nwp5wV2xZ6Eyt2iRtr0ustfVipE8ZEdL4RCpZYQMmj6mYXYx",
                timeout_s=3.0)
        search_results = yelp_api.search_query(term="coffee", location=location, sort_by='rating', limit=5)
        return render_template('search_results.html', search_results=search_results)


    return render_template('index.html', title=title, form=form)

# 127.0.0.1/search?q=coffee
@app.route("/search", methods=['POST'])
def search_results(search_dictionary):
   for i in search_dictionary:

    return render_template("search_results.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/new_account', methods=['GET', 'POST'])
def new_account():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('new_account.html', title='New Account', form=form)

@app.route('/my_account')
def my_account():
    title = 'My Account'
    return render_template('my_account.html', title=title)

@app.route('/add_shop')
def add_shop():
    title = 'Add Shop'
    return render_template('add_shop.html', title=title)