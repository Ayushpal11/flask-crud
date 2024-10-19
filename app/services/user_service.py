from flask import current_app
from bson import ObjectId
from datetime import datetime
from app.utils.password_utils import hash_password

class UserService:
    @staticmethod
    def get_all_users():
        return list(current_app.db.users.find())

    @staticmethod
    def get_user_by_id(user_id):
        return current_app.db.users.find_one({'_id': ObjectId(user_id)})

    @staticmethod
    def create_user(user_data):
        user_data['password'] = hash_password(user_data['password'])
        user_data['created_at'] = datetime.utcnow()
        user_data['updated_at'] = datetime.utcnow()
        result = current_app.db.users.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    def update_user(user_id, user_data):
        user_data['updated_at'] = datetime.utcnow()
        if 'password' in user_data:
            user_data['password'] = hash_password(user_data['password'])
        result = current_app.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': user_data})
        return result.modified_count > 0

    @staticmethod
    def delete_user(user_id):
        result = current_app.db.users.delete_one({'_id': ObjectId(user_id)})
        return result.deleted_count > 0