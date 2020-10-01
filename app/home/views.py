#Views for home page
from flask import abort, render_template, redirect,url_for
from flask_login import current_user, login_required

from . import home
@home.route('/')
def landingpage():
    """
    Render the landing home page template on the / route
    """
    return render_template('home/index.html', title="Welcome to the home page")
# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        return redirect(url_for("home.dataentry"))

    return render_template('home/dashboard.html', title="Dashboard")



@home.route('/dashboard')
def dataentry():
    """
    Render the dashboard page template on the /dashboard route
    """
    return render_template('home/dataentry.html', title="Welcome to the dashboard")   

@home.route('/products/add', methods=['GET', 'POST'])
@login_required
def add_product():
    """
    Add a product to the database
    """

    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.productname.data,
                                product_type=form.producttype.data,quantity=form.quantity.data,
                                status=form.status.data)
        try:
            # adding product to the database
            db.session.add(product)
            db.session.commit()
            flash('You have added a new product.')
        except:
            flash('Error: product name already exists.')

        

    return render_template('product.html', product_form = form)
                           

