from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import os
from dotenv import load_dotenv
import pymongo
from bson import ObjectId
import json

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_super_secret_key_change_in_production')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

# Initialize extensions
CORS(app, origins=os.getenv('ALLOWED_ORIGINS', '*').split(','))
jwt = JWTManager(app)

# Database configuration
db_type = os.getenv('DB_TYPE', 'mongodb')
if db_type == 'mongodb':
    client = pymongo.MongoClient(
        f"mongodb://{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '27017')}/"
    )
    db = client[os.getenv('DB_NAME', 'red_global_db')]
    users_collection = db['users']
    items_collection = db['items']
else:
    # MySQL configuration would go here
    pass

# Helper functions
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

app.json_encoder = JSONEncoder

def create_response(success, message, data=None, status=200):
    response = {
        'success': success,
        'message': message
    }
    if data:
        response['data'] = data
    return jsonify(response), status

# ==================== Authentication Routes ====================

@app.route('/api/auth/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Validate input
        if not data or not all(k in data for k in ('username', 'email', 'password')):
            return create_response(False, 'Missing required fields', None, 400)
        
        username = data['username']
        email = data['email']
        password = data['password']
        
        # Check if user already exists
        if users_collection.find_one({'email': email}):
            return create_response(False, 'Email already registered', None, 409)
        
        if users_collection.find_one({'username': username}):
            return create_response(False, 'Username already taken', None, 409)
        
        # Create new user
        user = {
            'username': username,
            'email': email,
            'password_hash': generate_password_hash(password),
            'created_at': None,
            'updated_at': None
        }
        
        result = users_collection.insert_one(user)
        
        return create_response(
            True, 
            'User registered successfully', 
            {'user_id': str(result.inserted_id)},
            201
        )
    
    except Exception as e:
        return create_response(False, f'Error: {str(e)}', None, 500)

@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        if not data or not all(k in data for k in ('email', 'password')):
            return create_response(False, 'Missing email or password', None, 400)
        
        email = data['email']
        password = data['password']
        
        # Find user
        user = users_collection.find_one({'email': email})
        
        if not user or not check_password_hash(user['password_hash'], password):
            return create_response(False, 'Invalid email or password', None, 401)
        
        # Create access token
        access_token = create_access_token(identity=str(user['_id']))
        
        return create_response(
            True,
            'Login successful',
            {
                'token': access_token,
                'user': {
                    'id': str(user['_id']),
                    'username': user['username'],
                    'email': user['email']
                }
            },
            200
        )
    
    except Exception as e:
        return create_response(False, f'Error: {str(e)}', None, 500)

@app.route('/api/auth/me', methods=['GET'])
@jwt_required()
def get_current_user():
    try:
        user_id = get_jwt_identity()
        user = users_collection.find_one({'_id': ObjectId(user_id)})
        
        if not user:
            return create_response(False, 'User not found', None, 404)
        
        return create_response(
            True,
            'User found',
            {
                'id': str(user['_id']),
                'username': user['username'],
                'email': user['email']
            },
            200
        )
    
    except Exception as e:
        return create_response(False, f'Error: {str(e)}', None, 500)

# ==================== Items Routes (CRUD) ====================

@app.route('/api/items', methods=['GET'])
@jwt_required()
def get_items():
    try:
        user_id = get_jwt_identity()
        items = list(items_collection.find({'user_id': user_id}))
        
        # Convert ObjectId to string
        for item in items:
            item['_id'] = str(item['_id'])
        
        return create_response(True, 'Items retrieved successfully', items, 200)
    
    except Exception as e:
        return create_response(False, f'Error: {str(e)}', None, 500)

@app.route('/api/items', methods=['POST'])
@jwt_required()
def create_item():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data or 'title' not in data:
            return create_response(False, 'Title is required', None, 400)
        
        item = {
            'user_id': user_id,
            'title': data['title'],
            'description': data.get('description', ''),
            'category': data.get('category', 'general'),
            'status': 'active',
            'created_at': None,
            'updated_at': None
        }
        
        result = items_collection.insert_one(item)
        item['_id'] = str(result.inserted_id)
        
        return create_response(
            True, 
            'Item created successfully', 
            item,
            201
        )
    
    except Exception as e:
        return create_response(False, f'Error: {str(e)}', None, 500)

@app.route('/api/items/<item_id>', methods=['GET'])
@jwt_required()
def get_item(item_id):
    try:
        user_id = get_jwt_identity()
        item = items_collection.find_one({
            '_id': ObjectId(item_id),
            'user_id': user_id
        })
        
        if not item:
            return create_response(False, 'Item not found', None, 404)
        
        item['_id'] = str(item['_id'])
        
        return create_response(True, 'Item retrieved successfully', item, 200)
    
    except Exception as e:
        return create_response(False, f'Error: {str(e)}', None, 500)

@app.route('/api/items/<item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        # Find item
        item = items_collection.find_one({
            '_id': ObjectId(item_id),
            'user_id': user_id
        })
        
        if not item:
            return create_response(False, 'Item not found', None, 404)
        
        # Update fields
        update_data = {}
        if 'title' in data:
            update_data['title'] = data['title']
        if 'description' in data:
            update_data['description'] = data['description']
        if 'category' in data:
            update_data['category'] = data['category']
        if 'status' in data:
            update_data['status'] = data['status']
        
        update_data['updated_at'] = None
        
        items_collection.update_one(
            {'_id': ObjectId(item_id)},
            {'$set': update_data}
        )
        
        updated_item = items_collection.find_one({'_id': ObjectId(item_id)})
        updated_item['_id'] = str(updated_item['_id'])
        
        return create_response(True, 'Item updated successfully', updated_item, 200)
    
    except Exception as e:
        return create_response(False, f'Error: {str(e)}', None, 500)

@app.route('/api/items/<item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    try:
        user_id = get_jwt_identity()
        
        result = items_collection.delete_one({
            '_id': ObjectId(item_id),
            'user_id': user_id
        })
        
        if result.deleted_count == 0:
            return create_response(False, 'Item not found', None, 404)
        
        return create_response(True, 'Item deleted successfully', None, 200)
    
    except Exception as e:
        return create_response(False, f'Error: {str(e)}', None, 500)

# ==================== Health Check ====================

@app.route('/api/health', methods=['GET'])
def health_check():
    return create_response(True, 'API is running', {'version': '1.0.0'}, 200)

@app.route('/', methods=['GET'])
def home():
    return create_response(
        True, 
        'Welcome to Red Global Assignment API', 
        {
            'version': '1.0.0',
            'endpoints': {
                'auth': ['/api/auth/register', '/api/auth/login', '/api/auth/me'],
                'items': ['/api/items']
            }
        }, 
        200
    )

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return create_response(False, 'Route not found', None, 404)

@app.errorhandler(500)
def internal_error(error):
    return create_response(False, 'Internal server error', None, 500)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'True') == 'True'
    app.run(host='0.0.0.0', port=port, debug=debug)
