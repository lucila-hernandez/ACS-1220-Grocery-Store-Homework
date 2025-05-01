from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, NumberRange
from grocery_app.models import GroceryStore


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField('Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80)
        ])
    address = StringField('Store Address', validators=[
            DataRequired(), 
            Length(min=3, max=200)
        ])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField(
        'Item Name',
        validators=[
            DataRequired(),
            Length(min=3, max=80)
        ]
    )

    price = FloatField(
        'Price',
        validators=[
            DataRequired(),
            NumberRange(min=0, message="Price must be non-negative")
        ]
    )

    category = SelectField(
        'Category',
        choices=[
            ('PRODUCE', 'Produce'),
            ('DELI', 'Deli'),
            ('BAKERY', 'Bakery'),
            ('PANTRY', 'Pantry'),
            ('FROZEN', 'Frozen'),
            ('OTHER', 'Other')
        ],
        validators=[DataRequired()]
    )

    photo_url = StringField(
        'Photo URL',
        validators=[
            DataRequired(),
            URL(message="Must be a valid URL"),
            Length(max=300)
        ]
    )

    store = QuerySelectField(
        'Store',
        query_factory=lambda: GroceryStore.query.all(),
        get_label='title',
        allow_blank=False
    )

    submit = SubmitField('Submit')
    
