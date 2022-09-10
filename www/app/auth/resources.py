from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import jwt_required, unset_jwt_cookies
from app.common.error_handling import ObjectNotFound
from app.users.models import User
from app.users.schemas import UserSchema

user_schema = UserSchema()

class LoginResource(Resource):

    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user is None:
            raise ObjectNotFound('User not found')
        if not user.check_password(data['password']):
            raise ObjectNotFound('Password is incorrect')
        access_token = create_access_token(identity=user_schema.dump(user))
        refresh_token = create_refresh_token(identity=user_schema.dump(user))
        return jsonify({"token": access_token, "refresh_token": refresh_token, "user": user_schema.dump(user)})

class LogoutResource(Resource):

    @jwt_required()
    def get(self):
        response = jsonify({'message':"Successfully Logged Out"})
        unset_jwt_cookies(response)
        return response
