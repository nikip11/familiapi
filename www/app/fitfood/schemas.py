from marshmallow import fields

from app.ext import ma

class FoodSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    kc_100 = fields.Integer(required=True)
    portion = fields.Integer(required=True)
    kc_portion = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
