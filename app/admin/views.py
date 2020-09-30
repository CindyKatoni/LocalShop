from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from . import admin
from forms import ProductForm,RoleForm
from .. import db
from ..models import Product,Role

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Product Views


@admin.route('/products', methods=['GET', 'POST'])
@login_required
def list_products():
    """
    List all products
    """
    check_admin()

    products = Product.query.all()

    return render_template('admin/products/products.html',
                           products=products, title="Products")


@admin.route('/products/add', methods=['GET', 'POST'])
@login_required
def add_product():
    """
    Add a product to the database
    """
    check_admin()

    add_product = True

    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data,
                                description=form.description.data,
                                status=form.status.data)
        try:
            # adding product to the database
            db.session.add(product)
            db.session.commit()
            flash('You have added a new product.')
        except:
            flash('Error: product name already exists.')

        
        return redirect(url_for('admin.list_products'))

    return render_template('admin/products/product.html', action="Add",
                           add_product=add_product, form=form,
                           title="Add Product")


@admin.route('/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    """
    Edit a product
    """
    check_admin()

    add_product = False

    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.status = form.status.data
        db.session.commit()
        flash('You have successfully edited the product.')

        
        return redirect(url_for('admin.list_products'))

    form.description.data = product.description
    form.name.data = product.name
    form.status.data = product.status
    return render_template('admin/products/product.html', action="Edit",
                           add_product=add_product, form=form,
                           product=product, title="Edit Product")






@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the role page
        return redirect(url_for('admin.list_roles'))

    # load role template 
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')



@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have deleted the role.')

    # redirect to the role page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")