from marshmallow import fields
from app.ext import ma

class TagSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    slug = fields.String(dump_only=True)

class CategorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
