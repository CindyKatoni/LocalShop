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
<<<<<<< HEAD
@login_required
=======
>>>>>>> main
def dataentry():
    """
    Render the dashboard page template on the /dashboard route
    """
    return render_template('home/dataentry.html', title="Welcome to the dashboard")    

<<<<<<< HEAD
@home.route('/request',methods = ["POST","GET"])
@login_required
def request():
    
    form = SupplyRequestForm()
    if form.validate_on_submit():
        productname = form.productname.data
        total_required = form.total_required.data

        new_request = SupplyRequest(productname=productname,total_required=total_required,user_id=current_user.id)
        db.session.add(new_request)
        db.session.commit()
        return redirect(url_for("home.dataentry"))

    return render_template('home/request.html', title="Create your request:", form=form)    
=======
>>>>>>> main
