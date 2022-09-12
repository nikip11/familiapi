from app.db import db, BaseModelMixin
from slugify import slugify

# tags
class Tag(db.Model, BaseModelMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(75), nullable=False)
    icon = db.Column(db.String(15), nullable=True)
    color = db.Column(db.String(15), nullable=True)

    def __init__(self, name):
        self.name = name
        self.slug = slugify(name)

    def __str__(self):
        return 'Tag %r' % self.name

    def __repr__(self):
        return '<Tag %r>' % self.name

# categories
class Category(db.Model, BaseModelMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(150), unique=True, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    alternates = db.relationship('Category', backref=db.backref('parent', remote_side=[id]))

    def __init__(self, name, image = '', parent_id = None):
        self.name = name
        self.slug = slugify(name)
        self.image = image
        self.parent_id = parent_id

    def __str__(self):
        return 'Category %r' % self.name

    def __repr__(self):
        return '<Category %r>' % self.name

# modules
# permissions
