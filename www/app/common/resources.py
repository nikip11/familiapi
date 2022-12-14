from flask import request
from flask_restful import Resource
from app.common.error_handling import ObjectNotFound
from .models import Category, Tag
from .schemas import TagSchema, CategorySchema

tag_schema = TagSchema()
category_schema = CategorySchema()

class TagResource(Resource):
    def get(self, name):
        tag = Tag.query.filter(Tag.name.like('%' + name + '%')).all()
        if tag is None:
            raise ObjectNotFound('Tag not found')
        return tag_schema.dump(tag, many=True)

    def delete(self, id):
        tag = Tag.query.get_or_404(id)
        tag.delete()
        return '', 204

class TagListResource(Resource):
    def get(self):
        tags = Tag.query.all()
        return tag_schema.dump(tags, many=True)

    def post(self):
        data = request.get_json()
        tag = Tag.query.filter_by(name=data['name']).first()
        if tag is None:
            tag_dict = tag_schema.load(data)
            tag = Tag(**tag_dict)
            tag.save()
        return tag_schema.dump(tag), 201

class CategoryResource(Resource):

    def get(self, id = None):
        if (id is None):
            categories = Category.query.all()
            return category_schema.dump(categories, many=True)
        category = Category.query.get_or_404(id)
        if category is None:
            raise ObjectNotFound('Category not found')
        return category_schema.dump(category)

    def put(self, id):
        category = Category.query.get_or_404(id)
        category_schema.load(request.json, instance=category)
        return category_schema.dump(category)

    def delete(self, id):
        category = Category.query.get_or_404(id)
        category.delete()
        return '', 204

    def post(self):
        data = request.get_json()
        category = Category.query.filter_by(name=data['name']).first()
        if category is None:
            category_dict = category_schema.load(data)
            category = Category(**category_dict)
            category.save()
        return category_schema.dump(category), 201

class CategoryParentResource(Resource):
    def __init__(self, **kwargs):
        self.parent = Category.query.filter_by(name=kwargs['parent']).first()
        if (self.parent is None):
            raise ObjectNotFound('Missing parent Category')

    def get(self, id = None):
        if (id is None):
            categories = Category.query.filter_by(parent=self.parent).all()
            return category_schema.dump(categories, many=True)

        category = Category.query.filter_by(parent=self.parent, id=id).first()
        if category is None:
            raise ObjectNotFound('Category not found')
        return category_schema.dump(category
        )
    # TDDO category update
    def put(self, id):
        category = Category.query.get_or_404(id)
        category_dict = category_schema.load(request.json)
        category = Category(**category_dict)
        category.update()
        return category_schema.dump(category)

    def delete(self, id):
        category = Category.query.get_or_404(id)
        category.delete()
        return '', 204

    def post(self):
        data = request.get_json()
        category = Category.query.filter_by(name=data['name']).first()
        if category is None:
            category_dict = category_schema.load(data)
            category = Category(**category_dict, parent=self.parent)
            category.save()
        return category_schema.dump(category), 201

