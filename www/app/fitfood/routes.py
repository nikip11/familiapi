from flask import Blueprint
from flask_restful import Api
from app.fitfood.types import FOOD_CATEGORY
from .resources import FoodResource, RecipeResource
from app.common.resources import CategoryParentResource

fitfood_blueprint = Blueprint('fitfood', __name__, url_prefix="/fitfood")
api = Api(fitfood_blueprint)

api.add_resource(FoodResource, '/food/<int:id>', '/food')
api.add_resource(RecipeResource, '/recipes/<int:id>', '/recipes')

api.add_resource(CategoryParentResource, '/categories/<int:id>', '/categories', resource_class_kwargs={'parent': FOOD_CATEGORY})
