from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from .models import Food, Recipe
from .schemas import FoodSchema, RecipeSchema

food_schema = FoodSchema()
recipe_schema = RecipeSchema()

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

class RecipeResource(Resource):

    def get(self, id = None):
        if (id is None):
            recipes = Recipe.query.all()
            return recipe_schema.dump(recipes, many=True)
        else:
            recipes = Recipe.query.get_or_404(id)
            return recipe_schema.dump(recipes, many=True)

    def delete(self, id):
        recipe = Recipe.query.get_or_404(id)
        recipe.delete()
        return '', 204

    def post(self):
        data = request.get_json()
        recipe_dict = recipe_schema.load(data)
        recipe = Recipe(**recipe_dict)
        recipe.save()
        return recipe_schema.dump(recipe)

