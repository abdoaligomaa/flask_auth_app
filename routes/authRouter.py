from flask import Blueprint ,jsonify, request
from marshmallow import ValidationError
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt,
    current_user,
    get_jwt_identity,
)
from models.userModle import User
from schema.schemas import UserSchema,LoginSchema

auth_bp=Blueprint('auth',__name__)

@auth_bp.post('/register')
def register():
    schema = UserSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    
    data=request.get_json()
    print(data)
    user= User.get_user_by_email(email=data.get('email'))
    if user is not None:
        return jsonify({'message':"user already exist"}),400
    new_user=User(first_name=data.get('first_name'),last_name=data.get('last_name'),email=data.get('email'),phone_number=data.get('phone_number'),is_admin=data.get('is_admin'))
    new_user.set_password(password=data.get('password'))
    new_user.save()
    
    result=UserSchema().dump(new_user)
    return {"message":"user is created","user":result} ,202

@auth_bp.post("/login")
def login_user():

    schema = LoginSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    
    data = request.get_json()

    user = User.get_user_by_email(email=data.get("email"))
    
    if user is None:
        return jsonify({"error": "Invalid email"}), 400


    if user and (user.check_password(password=data.get("password"))):
        access_token = create_access_token(identity={"id":user.id}, expires_delta=False)

        return (
            jsonify(
                {
                    "message": "Logged In ",
                    "access": access_token, 
                }
            ),
            200,
        )

    return jsonify({"error": "Invalid password"}), 400
