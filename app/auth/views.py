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
<<<<<<< HEAD
=======
    
>>>>>>> main
@auth.route('/logout')
@login_required
def logout():
    logout_user()
<<<<<<< HEAD
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
=======
    return redirect(url_for("home.landingpage"))
>>>>>>> main
