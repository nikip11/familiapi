from flask import Blueprint
from flask_restful import Api
from app.auth.resources import LoginResource, LogoutResource

auth_blueprint = Blueprint('auth', __name__)
api = Api(auth_blueprint)

api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')
