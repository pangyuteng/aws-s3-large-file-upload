import os
import sys
import traceback
import json
import time
import uuid
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS

import boto3
from botocore.client import Config

# THIS_DIR = os.path.dirname(os.path.abspath(__file__))
# settings_json_file = os.path.join(THIS_DIR,"zappa_setting.json")
# with open(settings_json_file,"r") as f:
#     content = json.loads(f.read())
# BUCKET_NAME = content["lambda_docker_flask"]["s3_bucket"]
BUCKET_NAME = "lambda-docker-flask-2405fd329144"

app = Flask(__name__)
CORS(app)

@app.route("/")
def serve():
    return jsonify(success=True)

@app.route("/time")
def get_current_time():
    return {"time": round(time.time())}

def get_s3_post_url(object_name):
    fields = None
    conditions = None
    expiry_time = 3600
    # The response contains the presigned URL and required fields
    s3_client = boto3.client("s3",
        config=Config(signature_version="s3v4")
    )
    url = s3_client.generate_presigned_post(
        BUCKET_NAME,
        object_name,
        Fields=fields,
        Conditions=conditions,
        ExpiresIn=expiry_time,
    )
    return url

@app.route("/upload")
def upload():
    # render upload page
    uid = uuid.uuid4().hex
    url_dict = get_s3_post_url(uid)
    return render_template('upload.html',uid=uid,url_dict=url_dict)

@app.route('/completed')
def completed():
    
    try:
        uid = request.args.get('uid')
        local_file_path = f"/tmp/{uid}"

        s3 = boto3.resource('s3')
        s3.Bucket(BUCKET_NAME).download_file(uid,local_file_path)
        df = pd.read_csv(local_file_path)
    except:
        error_dict = {"message":"unexpected error. traceback:"+traceback.format_exc()}
        return jsonify(error_dict)

    return render_template('completed.html',uid=uid,df=df)

#object_name: name of the file.
@app.route("/file-upload",methods=["GET"])
def file_upload():
    try:
        object_name = request.args.get('object_name')
    except:
        return jsonify({"message":"error: param `object_name` not specified!"})

    try:
        url_dict = get_s3_post_url(object_name)
        return url_dict
    except:
        traceback.print_exc()
        error_dict = {"message":"unexpected error. traceback:"+traceback.format_exc()}
        return jsonify(error_dict)
