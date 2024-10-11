from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    is_admin=fields.Boolean()

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)