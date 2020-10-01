from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,RadioField
from wtforms.validators import Length,DataRequired
from wtforms import ValidationError
from ..models import Product


class ProductForm(FlaskForm):

    productname = StringField('Enter Your Product Name', validators=[Length(min=1, max=20)])
    productspoilt = IntegerField('Number spoilt')
    quantity = IntegerField('Number of product Received')
    stock = IntegerField('Number of product in stock')
    status  = RadioField('Label', choices = [('paid', 'paid'), ('unpaid', 'unpaid')], validators = [DataRequired()])
    totalprice = IntegerField('Enter total price')
    submit = SubmitField('Submit')


 