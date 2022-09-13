from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from .models import Food
from .schemas import FoodSchema
from pprint import pprint

food_schema = FoodSchema()

class FoodResource(Resource):

    # @jwt_required()
    def get(self, id = None):
        if (id is None):
            foods = Food.query.all()
            return food_schema.dump(foods, many=True)
        else:
            food = Food.query.get_or_404(id)
            return food_schema.dump(food)

    # @jwt_required()
    def put(self, id):
        food = Food.query.get_or_404(id)
        food_schema.load(request.json, instance=food)
        return food_schema.dump(food)

    # @jwt_required()
    def delete(self, id):
        food = Food.query.get_or_404(id)
        food.delete()
        return '', 204

    def post(self):
        data = request.get_json()
        food_dict = food_schema.load(data)
        food = Food(**food_dict)
        food.save()
        return food_schema.dump(food), 201

