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


if __name__ == "__main__":
    app.run()