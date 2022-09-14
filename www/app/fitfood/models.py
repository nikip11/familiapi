from app.db import db, BaseModelMixin
from datetime import datetime
from sqlalchemy.dialects.mssql.base import VARCHAR

from app.common.models import Category

class Food(db.Model, BaseModelMixin):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    kc_100 = db.Column(db.Integer, nullable=False)
    portion = db.Column(db.Integer, nullable=True)
    kc_portion = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=True)

    # tags = db.relationship('Tag', secondary=food_tags, backref='food', cascade="all, delete")
    # recipes = db.relationship('RecipeIngredient', back_populates='food')

    def __init__(self, name, kc_100, portion, kc_portion, category):
        print(category['name'], '====')
        self.name = name
        self.kc_100 = kc_100
        self.portion = portion
        self.kc_portion = kc_portion
        if (category):
            self.category = Category.query.filter_by(id=category['id']).first()

    def __str__(self):
        return 'Food %r' % self.name

    def __repr__(self):
        return '<Food %r>' % self.name

class Recipe(db.Model, BaseModelMixin):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    preparation = db.Column(VARCHAR(1000), nullable=True)
    time = db.Column(db.String(10), nullable=True)
    image = db.Column(db.String(20), nullable=False, default='book-default.jpg')
    link = db.Column(db.String(120), nullable=True)
    kalories = db.Column(db.Integer, nullable=False)
    portions = db.Column(db.String(100), nullable=True)

    def __init__(self, name, preparation = '', time = '', image = '', link = '', kalories = '', portions = ''):
        self.name = name
        self.preparation = preparation
        self.time = time
        self.image = image
        self.link = link
        self.kalories = kalories
        self.portions = portions

    def __str__(self):
        return 'Recipe %r' % self.name

    def __repr__(self):
        return '<Recipe %r>' % self.name

# class RecipeIngredient(db.Model):
#     __tablename__ = 'recipe_ingredient'
#     recipe_id = db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id', ondelete='cascade'), primary_key=True)
#     food_id = db.Column('food_id', db.Integer, db.ForeignKey('food.id', ondelete='cascade'), primary_key=True)
#     weight = db.Column('weight', db.Integer)
#     portion = db.Column('portion', db.String(50))
#     unit = db.Column('unit', db.String(10))
#     food = db.relationship('Food', back_populates='recipes')
#     recipe = db.relationship('Recipe', back_populates='ingredients')

#     def __repr__(self):
#         return f"RecipeIngredient('{self.recipe_id}', '{self.food_id}','{self.weight}','{self.portion}')"

# recipe_tags = db.Table('recipe_tags',
#     db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
# )
