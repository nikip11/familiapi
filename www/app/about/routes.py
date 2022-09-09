from flask import Blueprint
from flask_restful import Api
from .resources import SkillsResource, WorksResource, CoursesResource

about_blueprint = Blueprint('about', __name__, url_prefix='/about')
api = Api(about_blueprint)
# 
api.add_resource(SkillsResource, '/skills')
api.add_resource(WorksResource, '/works')
api.add_resource(CoursesResource, '/courses')
