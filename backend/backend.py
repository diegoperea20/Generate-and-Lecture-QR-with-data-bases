from flask import Flask , request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Para usar fronted
from flask_cors import CORS
#------------------------------

#Para autentificar
from flask_bcrypt import check_password_hash, generate_password_hash
import jwt
import datetime
#------------------------------

app = Flask(__name__)

#Para usar fronted
CORS(app)
#---------

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypassword@localhost:3306/flaskmysql'
#app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://postgres:mypassword@localhost:5432/flaskpostgresql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db=SQLAlchemy(app)


ma= Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    user= db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, email, user, password):
        self.email = email
        self.user = user
        self.password = password
        


with app.app_context():
    db.create_all()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'user', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)




@app.route('/loginup', methods=['POST'])
def create_user():
    email=request.json['email']
    user=request.json['user']
    password = generate_password_hash(request.json['password'])
    existing_user = User.query.filter_by(user=user).first()
    if existing_user:
        return jsonify({'error': 'User already exists'}), 409
    new_user = User(email, user, password)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@app.route('/qr', methods=['GET'])
def get_qr_users():
    all_users = User.query.all()
    user_names = [user.user for user in all_users]  # Use 'user.user' instead of 'User.user'
    return jsonify(user_names)




@app.route('/loginup', methods=['GET'])
def get_users():
    all_users=User.query.all()
    result=users_schema.dump(all_users)
    return jsonify(result)                    

@app.route('/loginup/<id>', methods=['GET'])
def get_user(id):
    user=User.query.get(id)
    return user_schema.jsonify(user) 

@app.route('/loginup/<id>', methods=['PUT'])
def update_user(id):
    user_to_update = User.query.get(id)  # Renombrar la variable aquí
    
    email = request.json['email']
    new_user = request.json['user']
    password = generate_password_hash(request.json['password'])

    user_to_update.email = email
    user_to_update.user = new_user  # Renombrar la variable aquí
    user_to_update.password = password
    
    db.session.commit()
    return user_schema.jsonify(user_to_update)



@app.route('/loginup/<id>', methods=['DELETE'])
def delete_user(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)


#Comands for use docker container mysql
#docker run --name mymysql -e MYSQL_ROOT_PASSWORD=mypassword -p 3306:3306 -d mysql:latest
#docker exec -it mymysql bash
#mysql -u root -p
#create database flaskmysql;