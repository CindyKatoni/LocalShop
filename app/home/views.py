#Views for home page
from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def landingpage():
    """
    Render the landing home page template on the / route
    """
    return render_template('home/index.html', title="Welcome to the home page")

@home.route('/dashboard')
# @login_required #add later
def merchantdashboardpage():
    """
    Render the dashboard page template on the /dashboard route
    """
    return render_template('home/merchantdashboard.html', title="Welcome Merchant")    