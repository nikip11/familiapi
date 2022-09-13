from app.db import db, BaseModelMixin
from datetime import datetime

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
    # parent_slug='calorias'

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
