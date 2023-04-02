from flask import Flask, request
from flask_pymongo import PyMongo



app  = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://root:123456@localhost:27017/pythonmongodb?authSource=admin'
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/user', methods=['POST'])
def create_user():
    #reciving data
    user_name = request.json['user_name']
    passw = request.json['passw']
    email = request.json['email']
    mongo.db.user.insert_one({
        'user_name': user_name,
        'passw': passw,
        'email': email
    })
    
    return {'message': 'received'}

if __name__ == '__main__':
    app.run(debug=True)