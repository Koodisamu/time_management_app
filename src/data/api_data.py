from flask import Flask, request
from api_service import db_get_consultant, db_get_customer, db_log_hours
import json
from datetime import datetime



app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/consultants', methods=['GET'])
def get_all_consultants():
    try:  
        return db_get_consultant()
    except:
        return {"error": "no data"}
    
@app.route('/customers', methods=['GET'])
def get_all_customers():
    try:  
        return db_get_customer()
    except:
        return {"error": "no data"}
    
@app.route("/log_hours", methods=['POST'])
def log_hours():
    try: 
        data = request.get_json()
        consultant_id = data['consultant_id']
        customer_id = data['customer_id']
        startTime = datetime.fromisoformat(data['startTime'])  # Expect ISO 8601 format
        endTime = datetime.fromisoformat(data['endTime'])
        lunchbreak = data['lunchbreak']
        db_log_hours(consultant_id, customer_id, startTime, endTime, lunchbreak)
        return {"success": "logged hours for consultant id: %s " % consultant_id}
    except Exception as e:
        return {"error": "error logging hours", "exception": str(e)}


# @app.route('/attributes/<int:id>', methods=['GET'])
# def get_attribute_by_id(id):
#     try:
#         return db_get_attribute_by_id(id)
#     except:
#         return {"error": "no attribute with id %s" % id}

# @app.route("/attributes", methods=['POST'])
# def create_attribute():
#     try: 
#         data = request.get_json()
#         attribute_name = data['attribute_name']
#         attribute_description = data['attribute_description']
#         attribute_value = data['attribute_value']
#         person_id = data['person_id']
#         db_create_attribute(attribute_name, attribute_description, attribute_value, person_id)
#         return {"success": "created attribute: %s" % attribute_name}
#     except:
#         return {"error": "error creating attribute"}

# @app.route("/attributes/<int:id>", methods=['PUT'])
# def update_attribute(id):
#     try:
#         data = request.get_json()
#         attribute_name = data['attribute_name']
#         attribute_description = data['attribute_description']
#         attribute_value = data['attribute_value']
#         person_id = data['person_id']
#         db_update_attribute(id, attribute_name, attribute_description, attribute_value, person_id)
#         return {"success": "updated attribute"}
#     except:
#         return {"error": "error updating attribute"}

# @app.route('/attributes/<int:id>', methods=['DELETE'])
# def delete_attribute(id):
#     try:
#         return db_delete_attribute(id)
#     except:
#         return {"error": "no such atttribute"}   

if __name__ == "__main__":
    app.run()