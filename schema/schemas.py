from marshmallow import Schema, fields,validates,ValidationError
import re 

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    is_admin=fields.Boolean()

    @validates('password')
    def validate_password(self, value):
        # Example regular expression pattern
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

        if not re.match(pattern, value):
            raise ValidationError("Password must be at least 8 characters and include uppercase, lowercase, numbers, and symbols (optional)")
    

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)