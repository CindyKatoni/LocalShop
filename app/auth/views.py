# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, UserRegistrationForm
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=form.password.data)

        # add employee to the database
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered! Check your email for login credentials.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register a new user.')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
                form.password.data):
            # log user in
            login_user(user)
from flask import render_template,flash, request, redirect, url_for
from flask_login import login_user, logout_user,login_required
from app.auth import auth
from app.models import User
from .. import db
from .forms import RegForm,LoginForm


@auth.route('/login',methods = ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user != None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            flash('Wrong Username or Password')
             # redirect to the appropriate dashboard page
            if User.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dataentry'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/signup',methods = ["POST","GET"])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,first_name=form.firstname.data,last_name=form.lastname.data, email = form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit() #initialised this
        mail_message("Welcome to Local Shop",user.email,user=user)
        return  redirect(url_for('auth.login'))
    return render_template('auth/signup.html',registration_form=form )
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.landingpage"))
            # redirect to the dashboard page after login
            return redirect(url_for('home.dashboardpage'))

        # when login details are incorrect
        else:
            flash('Unauthorized login attempt.')
            return redirect(url_for('home.landingpage'))

    # load login template
    return render_template('auth/login.html', form=form, title='Dashboard Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('home.landingpage'))
