from models.verb_model import Verb
from database.__init__ import conn
import app_config as config
import requests as requests
from bson import ObjectId


def get_verb_from_api(verb_information): # Function to get a verb
    try: 
        external_api_url = config.CONST_URL_API_LASALLE + "/verb" # URL of the external API
        response = requests.get(external_api_url, headers={ # Request to the external API
                                'token': config.CONST_TOKEN_API_LASALLE}, json={'verb': verb_information['verb']}) # Headers and data of the request

        if response.status_code == 200: # Check if the request was successful
            return {"verb": response.json(), "status_code": response.status_code} 
        else: 
            return {"error": "Error on getting verb.", "status_code": response.status_code} 
    except Exception as err: 
        raise ValueError("Error on trying to getting verb.", err) 


def create_favorite_verbs(data_information):
    try:
        new_verb = Verb()
        new_verb.owner = data_information["owner"]
        new_verb.verb = data_information["verb"]

        db_collection = conn.database[config.CONST_VERBS_COLLECTION]
        created_verb = db_collection.insert_one(new_verb.__dict__)

        return created_verb
    except Exception as err:
        raise ValueError("Error on creating favorite verb.", err)


def fetch_fav_verbs(favorite_id):
    try:
        db_collection = conn.database[config.CONST_VERBS_COLLECTION]
        favorite_id_obj = ObjectId(favorite_id)

        # Converte o cursor em uma lista de dicionários
        fav_verbs = list(db_collection.find({'_id': favorite_id_obj}))

        # Converte o ObjectId para string antes de retornar
        for verb in fav_verbs:
            verb['_id'] = str(verb['_id'])

        return fav_verbs
    except Exception as err:
        raise ValueError("Error on fetching favorite verbs.", err)


def fetch_all_verbs(user_information):
    try:
        print("Entrou fetch all")
        db_collection = conn.database[config.CONST_VERBS_COLLECTION]
        user_favorite_verbs_list = []

        for verb_doc in db_collection.find({'owner': user_information['id']}):
            user_favorite_verbs = {}
            user_favorite_verbs["_id"] = str(verb_doc["_id"])
            user_favorite_verbs["owner"] = verb_doc["owner"]
            user_favorite_verbs["verbs"] = verb_doc["verb"]
            user_favorite_verbs_list.append(user_favorite_verbs)

        return user_favorite_verbs_list

    except Exception as err:
        raise ValueError("Error on trying to fetch users.", err)


def get_random_verbs_from_api(quantity):
    try:
        external_api_url = config.CONST_URL_API_LASALLE + "/verb/random"
        response = requests.get(external_api_url, headers={
                                'token': config.CONST_TOKEN_API_LASALLE}, json={'quantity': quantity})

        if response.status_code == 200:
            return {"verb": response.json(), "status_code": response.status_code}
        else:
            return {"error": "Error on getting verb.", "status_code": response.status_code}
    except Exception as err:
        raise ValueError("Error on trying to getting verb.", err)


def delete_favorite_verb_by_id(favorite_id, user_id):
    try:
        db_collection = conn.database[config.CONST_VERBS_COLLECTION]
        favorite_id_obj = ObjectId(favorite_id)

        # Ensures that only the owner can delete the verb
        delete_result = db_collection.delete_one(
            {'_id': favorite_id_obj, 'owner': user_id})

        return delete_result
    except Exception as err:
        raise ValueError("Error on deleting favorite verb.", err)
