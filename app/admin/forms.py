from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Product, Role


class ProductForm(FlaskForm):
    """
    Form for admin to add or edit product
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


# existing code remains

class UserAssignForm(FlaskForm):
    """
    Form for admin to assign roles to users
    """
    
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')