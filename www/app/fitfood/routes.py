from flask import Blueprint
from flask_restful import Api
from .resources import FoodResource, FoodListResource

fitfood_blueprint = Blueprint('fitfood', __name__, url_prefix="/fitfood")
api = Api(fitfood_blueprint)

api.add_resource(FoodResource, '/food/<int:id>')
api.add_resource(FoodListResource, '/food')
