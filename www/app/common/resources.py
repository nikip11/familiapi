from flask import request
from flask_restful import Resource
from app.common.error_handling import ObjectNotFound
from .models import Tag
from .schemas import TagSchema

tag_schema = TagSchema()

class TagResource(Resource):
    def get(self, name):
        tag = Tag.query.filter(Tag.name.like('%' + name + '%')).all()
        print(name, tag)
        if tag is None:
            raise ObjectNotFound('Tag not found')
        return tag_schema.dump(tag, many=True)

    def delete(self, name):
        tag = Tag.query.get_or_404(name)
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
