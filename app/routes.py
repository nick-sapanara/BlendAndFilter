from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, RegistrationForm2, RegistrationForm3, AddShopForm
from app.models import User, Shop, Tag, User2Tag


@app.route('/')
@app.route('/index')
def index():
    title = 'Blend & Filter'
    return render_template('index.html', title=title)

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
        if form.validate_on_submit():
            user = User(name=form.name.data,
                        username=form.username.data,
                        email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
        return redirect(url_for('new_account2'))
    return render_template('new_account.html', title='New Account', form=form)


@app.route('/new_account2', methods=['GET', 'POST'])
@login_required
def new_account2():
    form = RegistrationForm2()
    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('new_account3'))
    return render_template('new_account.html', title='New Account', form=form)


@app.route('/new_account3', methods=['GET', 'POST'])
@login_required
def new_account3():
    form = RegistrationForm3()
    form.tag.choices = [(t.id, t.coffee) for t in Tag.query.all()]
    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        for tag_id in form.tag.data:
            u2t = User2Tag(user=user, tag_id=tag_id)
            db.session.add(u2t)
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_account.html', title='New Account', form=form)


@app.route('/my_account')
@login_required
def my_account(username):
    my_account = User.query.filter_by(username=username).first_or_404()
    if my_account is None:
        flash('That game does not exist in the database')
        return redirect(url_for('index'))
    return render_template('my_account.html', title='My Account', my_account=my_account)


@app.route('/add_shop')
@login_required
def add_shop():
    form = AddShopForm()
    if form.validate_on_submit():
        shop = Shop(shopName=form.shopName.data,
                    ownerName=form.ownerName.data,
                    address=form.address.data,
                    website=form.website.data,
                    about_shop=form.about_shop.data)
        db.session.add(shop)
        db.session.commit()
        return redirect(url_for('shop'))
    return render_template('add_shop.html', title='Add Shop', form=form)

@app.route('/shop')
@login_required
def shop():

    return render_template('shop.html', title='Shop')

@app.route("/populate_db")
def populate_db():
    clear_db()

    u1 = User(name="Nick", username="nsap", email="nsapanara@ithaca.edu")
    u2 = User(name="Cam", username="cammax", email="cm@ithaca.edu")
    u3 = User(name="Claire", username="clairet", email="ct@ithaca.edu")
    db.session.add_all([u1, u2, u3])
    db.session.commit()

    t1 = Tag(coffee="Dark Roast")
    t2 = Tag(coffee="Medium Roast")
    t3 = Tag(coffee="Light Roast")
    t4 = Tag(coffee="Espresso")
    t5 = Tag(coffee="Latte")
    t6 = Tag(coffee="Cold Brew")
    db.session.add_all([t1, t2, t3, t4, t5, t6])
    db.session.commit()

    u2t1 = User2Tag(user_id="1", tag_id="1")
    u2t2 = User2Tag(user_id="1", tag_id="2")
    u2t3 = User2Tag(user_id="1", tag_id="5")
    u2t4 = User2Tag(user_id="2", tag_id="1")
    u2t5 = User2Tag(user_id="2", tag_id="2")
    u2t6 = User2Tag(user_id="2", tag_id="4")
    u2t7 = User2Tag(user_id="3", tag_id="6")
    db.session.add_all([u2t1, u2t2, u2t3, u2t4, u2t5, u2t6, u2t7])
    db.session.commit()

    flash("Database has been populated")
    return render_template('index.html', title='Home')


def clear_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")
   # clear all data from all tables
   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()
   return render_template('index.html', meta=meta)
