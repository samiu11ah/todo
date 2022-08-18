from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

from flask_login import current_user
from .models import Category




class TodoForm(FlaskForm):
    priorities = [
        ('0', 'None'),
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'),
    ]
    title = StringField("Todo")
    priority = SelectField('Priority', choices=priorities)
    # category = SelectField("Category")

    # def __init__(self):
    #     super(TodoForm, self).__init__()
    #     self.category.choices = [(c.id, f'{c.name} - color: {c.color}') for c in Category.query.filter_by(user=current_user)]

class CategoryForm(FlaskForm):
    name = StringField("Category Name")

