from flask import request
from flask_restx import Namespace, Resource, fields
from app.models.user import user_schema, users_schema
from app.services.user_service import UserService
from marshmallow import ValidationError

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('')
class UserList(Resource):
    @api.doc('list_users')
    def get(self):
        """List all users"""
        users = UserService.get_all_users()
        return users_schema.dump(users)

    @api.doc('create_user')
    @api.expect(user_model)
    def post(self):
        """Create a new user"""
        try:
            user_data = user_schema.load(request.json)
            user_id = UserService.create_user(user_data)
            return {'message': 'User created successfully', 'id': user_id}, 201
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, 400

@api.route('/<string:user_id>')
@api.param('user_id', 'The user identifier')
class User(Resource):
    @api.doc('get_user')
    def get(self, user_id):
        """Fetch a user by ID"""
        user = UserService.get_user_by_id(user_id)
        if user:
            return user_schema.dump(user)
        api.abort(404, f"User {user_id} not found")

    @api.doc('update_user')
    @api.expect(user_model)
    def put(self, user_id):
        """Update a user"""
        try:
            user_data = user_schema.load(request.json, partial=True)
            if UserService.update_user(user_id, user_data):
                return {'message': 'User updated successfully'}
            api.abort(404, f"User {user_id} not found")
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, 400

    @api.doc('delete_user')
    def delete(self, user_id):
        """Delete a user"""
        if UserService.delete_user(user_id):
            return {'message': 'User deleted successfully'}
        api.abort(404, f"User {user_id} not found")