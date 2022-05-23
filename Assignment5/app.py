from flask import Flask, render_template, url_for, redirect, flash, request
from forms import RegistrationForm, LoginForm
from api import Crypto
from config import db, app
from models import User

crypto = Crypto()

@app.route("/")
@app.route("/home", methods=['POST', 'GET'])
def home():
    user_location = crypto.get_ip_loc()
    # returns the formatted price of the coins in USD
    results1 = crypto.get_top_1()
    results20 = crypto.get_top_20()
    for result in results20:
        result['quote']['USD']['price'] = '$ ' + "{:.2f}".format(result['quote']['USD']['price'])
    for result in results1:
        result['quote']['USD']['price'] = '$ ' + "{:.2f}".format(result['quote']['USD']['price'])

    return render_template('home.html', title='home', **locals())

@app.route("/mywatchlist", methods=['POST', 'GET'])
def mywatchlist():
    return render_template('mywatchlist.html', title='my-watch-list', **locals())

@app.route("/faq")
def faq():
    return render_template('faq.html', title='faq', **locals())

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully', category='success')
        return redirect(url_for('login'))
    return render_template('signup.html', title='signup', form=form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and form.password.data==user.password:
            flash('Login successful', category='success')
            return redirect(url_for('mywatchlist'))
        else: 
            flash('Login Unsuccessful', category='danger')  
            return redirect(url_for('login'))     
    return render_template('login.html', title='login', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
