from flask import Blueprint
from flask_restful import Api
from .resources import TagResource, TagListResource

commons_blueprint = Blueprint('commons', __name__)
api = Api(commons_blueprint)

api.add_resource(TagResource, '/tags/<string:name>')
api.add_resource(TagListResource, '/tags')

# api.add_resource(CategoryResource, '/categories/<int:id>')
# api.add_resource(CategoryListResource, '/categories')
