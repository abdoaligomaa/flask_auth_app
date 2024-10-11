from flask import Flask ,jsonify
from extensions import db,jwt
from routes.authRouter import auth_bp
from routes.userRouter import user_bp

def create_app():

    app=Flask(__name__)
    
    app.config.from_prefixed_env() # this will take the variables from .env file

    # intioalization
    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    # register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)

    # jwt error handlers 
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header,jwt_data):
        return jsonify({"message":"Token has expired","error":"Token expired"})
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"message":"Invalid jwt token","error":"invalid token"})

    @jwt.unauthorized_loader
    def unauthorized_callback(error):
        return jsonify({"message":"please provide autherize token","error":"unauthorized"})


    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
