from flask import Blueprint
from flask_restful import Api
from .resources import FoodResource
from app.common.resources import CategoryParentResource

fitfood_blueprint = Blueprint('fitfood', __name__, url_prefix="/fitfood")
api = Api(fitfood_blueprint)

api.add_resource(FoodResource, '/food/<int:id>', '/food')

api.add_resource(CategoryParentResource, '/categories/<int:id>', '/categories', resource_class_kwargs={'parent': 'fitfood'})
