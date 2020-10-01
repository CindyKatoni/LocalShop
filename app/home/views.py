#Views for home page
from flask import abort, render_template, redirect,url_for
from flask_login import current_user, login_required

from . import home

# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        return redirect(url_for("home.dataentry"))

    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/')
def landingpage():
    """
    Render the landing home page template on the / route
    """
    return render_template('home/index.html', title="Welcome to the home page")

@home.route('/dashboard')
def dataentry():
    """
    Render the dashboard page template on the /dashboard route
    """
    return render_template('home/dataentry.html', title="Welcome to the dashboard")    

