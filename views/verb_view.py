from flask import Blueprint, jsonify, request
from models.user_model import User
from controllers.verbs_controller import get_verb_from_api, create_favorite_verbs, fetch_fav_verbs, fetch_all_verbs,get_random_verbs_from_api, delete_favorite_verb_by_id
from database.__init__ import conn
import helpers.token_validation as token_validation
import json
from helpers.token_validation import validate_jwt

verb = Blueprint("verbs", __name__) 

@verb.route("/verbs/", methods=["GET"]) # GET method to get a verb
def get_verb(): 
    try: 
        user_information = validate_jwt() # Validate the token

        if user_information == 400: 
            return jsonify({'error': 'Token is missing in the request.'}), 400 
        if user_information == 401: 
            return jsonify({'error': 'Token is invalid.'}), 401 
        if user_information == 403: 
            return jsonify({'error': 'Token is expired.'}), 403 
        
        data = json.loads(request.data) # Load the data from the request

        if 'verb' not in data: 
            return jsonify({'error': 'Verb is needed in the request.'}), 400 
        
        get_verb = get_verb_from_api(data) # Call the function to get the verb

        return jsonify({"verb": get_verb}) # Return the verb
    except ValueError: 
        return jsonify({'error': 'Error on getting verb.'}), 500 


@verb.route("/verbs/favorites/", methods=["POST"])
def add_favorite_verb():
    try:
        user_information = validate_jwt()
        user_id = user_information['id']

        if user_information == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 400
        if user_information == 401:
            return jsonify({'error': 'Token is invalid.'}), 401
        if user_information == 403:
            return jsonify({'error': 'Token is expired.'}), 403
        
        data = json.loads(request.data)
        if 'verb' not in data:
            return jsonify({'error': 'Verb is needed in the request.'}), 400

        get_verb = get_verb_from_api(data)
        if get_verb["status_code"] == 200:

            favorite_data = {"owner": user_id, "verb": data["verb"]}
            create_verb = create_favorite_verbs(favorite_data)

            if create_verb == "Duplicated Verb":
                return jsonify({'error': 'There is already a favorite verb with this name.'}), 400
        return jsonify({'id': str(create_verb.inserted_id)})
    except ValueError:
        return jsonify({'error': 'Error on adding favorite verb.'}), 500
    
@verb.route("/verbs/favorites/<favoriteUid>", methods=["GET"])
def get_one_favorite_verb(favoriteUid):
    try:
        user_information = validate_jwt()

        if user_information == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 400
        if user_information == 401:
            return jsonify({'error': 'Token is invalid.'}), 401
        if user_information == 403:
            return jsonify({'error': 'Token is expired.'}), 403
        
        favorite_verb = fetch_fav_verbs(favoriteUid)
       
        return jsonify({'favorite_verb': favorite_verb})
    except ValueError:
        return jsonify({'error': 'Error on getting favorite verb.'}), 500


@verb.route("/verbs/favorites/", methods=["GET"])
def get_all_favorite_verb():
    try:
        print("Entrou get all")
        user_information = validate_jwt()
        
        if user_information == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 400
        if user_information == 401:
            return jsonify({'error': 'Token is invalid.'}), 401
        if user_information == 403:
            return jsonify({'error': 'Token is expired.'}), 403
        
        #user_id = user_information['id']
        favorite_verb = fetch_all_verbs(user_information)
       
        return jsonify({'favorite_verb': favorite_verb})
    except ValueError:
        return jsonify({'error': 'Error on getting favorite verb.'}), 500
    
@verb.route("/verbs/random", methods=["GET"])
def get_random_verb():
    try:
        user_information = validate_jwt()

        if user_information == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 400
        if user_information == 401:
            return jsonify({'error': 'Token is invalid.'}), 401
        if user_information == 403:
            return jsonify({'error': 'Token is expired.'}), 403       
        
        
        request_data = request.get_json()

        if 'quantity' not in request_data:
            return jsonify({'error': 'Quantity is needed in the request.'}), 400
        
        quantity = request_data["quantity"]
        get_verb = get_random_verbs_from_api(quantity)

        return jsonify({"verb": get_verb})
    except ValueError:
        return jsonify({'error': 'Error on getting verb.'}), 500

@verb.route("/verbs/favorites/<favoriteUid>", methods=["DELETE"])
def delete_favorite_verb(favoriteUid):
    try:
        user_information = validate_jwt()

        if user_information in [400, 401, 403]:
            return jsonify({'error': 'Token error. Please check your token.'}), user_information

        delete_result = delete_favorite_verb_by_id(favoriteUid, user_information['id'])

        if delete_result.deleted_count == 0:
            return jsonify({'error': 'No favorite verb found with the provided ID or you are not authorized to delete this verb.'}), 404

        return jsonify({'message': 'Favorite verb deleted successfully.'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 500
