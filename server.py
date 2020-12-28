from flask import Flask, render_template, redirect, url_for, request, Response
import os
import time
import json
from flask_sqlalchemy import SQLAlchemy
from models.recognization import db
from models.recognization import face_recognization as Log


app = Flask(__name__)
def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///face_recognization.db'
    db = SQLAlchemy(app)

@app.route("/", methods=["GET"])
def get_face_recognization():
    """
    Get face recognizations from person id and camera id
    """
    params = request.args
    if 'personID' not in params:
        return Response('personID not in arguments', status=400)
    
    if 'camID' not in params:
        return Response('camID not in arguments', status=400)

    person_id = str(params.get('personID'))
    cam_id = str(params.get('camID'))
    time_from = int(params.get('timeFrom')) if 'timeFrom' in params else 0
    time_to = int(params.get('timeTo')) if 'timeTo' in params else int(round(time.time() * 1000))
    results = Log.query.filter(Log.person_id == person_id).filter(Log.cam_id == cam_id).filter(Log.timestamp <= time_to).filter(Log.timestamp >= time_from).all()

    output = []
    for result in results:
        output.append(result.to_dict(request.base_url))
    return json.dumps(output)


if __name__ == "__main__":
    create_app()
    app.run()
 
