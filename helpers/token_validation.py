import jwt
from flask import request
import app_config as config

def validate_jwt():
    token = None
    user_information = None
    try:
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return 400 
        try:
            user_information = jwt.decode(token, config.TOKEN_SECRET, algorithms = ["HS256"])
        except Exception:
            return 401
        
        return user_information

    except jwt.ExpiredSignatureError:
        return 401
    except:
        return 400