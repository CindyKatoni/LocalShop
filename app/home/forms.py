from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import SupplyRequest

class SupplyRequestForm(FlaskForm):
    """
    Form for data clerk to request for product supply
    """
    productname = StringField('Product Name:', validators=[DataRequired()])
    total_required = IntegerField('Total Required:',validators=[DataRequired()])
    submit = SubmitField('Submit')