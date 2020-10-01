from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import Length
from wtforms import ValidationError
from ..models import Product


class ProductForm(FlaskForm):

    productname = StringField('Enter Your Product Name', validators=[Length(min=1, max=20)])
    producttype = StringField('Type of product', validators=[Length(min=1, max=20)])
    quantity = IntegerField('Number of product Received', validators=[Length(min=4, max=20)])
    status = StringField('Paid or Unpaid', validators=[Length(min=1, max=20)])
    submit = SubmitField('Submit')

 