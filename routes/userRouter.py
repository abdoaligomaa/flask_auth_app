from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from models.userModle import User
from schema.schemas import UserSchema
from flask_jwt_extended import get_jwt_identity



user_bp = Blueprint("users", __name__)


@user_bp.get("/all_users")
@jwt_required()
def getUser():
    current_user_id = get_jwt_identity() # will return the object which incoded while login 
    user = User.query.get(current_user_id)
    # result=UserSchema().dump(user) # if you try to send user object
    return f"hello ,{user.first_name}", 200 


@user_bp.get("/admin_only_page") 
@jwt_required()
def getAdmin():
    current_user_id = get_jwt_identity() # will return the object which incoded while login 
    user = User.query.get(current_user_id)
    if user is None:
         return jsonify({"error":"no user found"}), 404
    # print(user.first_name) 
    if not user.is_admin:
        return jsonify({"error": "Allowed only for admins"}), 403
    # result=UserSchema().dump(user)# if you try to send user object
    return f"hello ,{user.first_name}", 200 

@user_bp.get("/visitor") 
def visitor():
    return 'hello visitor', 200
    
