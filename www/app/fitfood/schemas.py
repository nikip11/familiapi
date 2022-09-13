from marshmallow import fields, Schema
from app.common.schemas import CategorySchema

from app.ext import ma

class FoodSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    kc_100 = fields.Integer(required=True)
    portion = fields.Integer(required=True)
    kc_portion = fields.Integer(required=True)
    category = fields.Nested(CategorySchema)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
