#Views for home page
from flask import abort, render_template
from flask_login import current_user, login_required

from . import home

@home.route('/')
def landingpage():
    """
    Render the landing home page template on the / route
    """
    return render_template('home/index.html', title="Welcome to the home page")

@home.route('/dashboard')
@login_required
def dashboardpage():
    """
    Render the dashboard page template on the /dashboard route
    """
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)
        
    return render_template('home/dashboard.html', title="Admin dashboard")    