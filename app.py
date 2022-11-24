import os
import sys
import traceback
import json
import time
import uuid
from flask import Flask, render_template, request, redirect, url_for, jsonify

import boto3
from botocore.client import Config

# THIS_DIR = os.path.dirname(os.path.abspath(__file__))
# settings_json_file = os.path.join(THIS_DIR,"zappa_setting.json")
# with open(settings_json_file,"r") as f:
#     content = json.loads(f.read())
# BUCKET_NAME = content["lambda_docker_flask"]["s3_bucket"]
BUCKET_NAME = "lambda-docker-flask-2405fd329144"

app = Flask(__name__)

@app.route("/")
def serve():
    return jsonify(success=True)

@app.route("/time")
def get_current_time():
    return {"time": round(time.time())}

@app.route("/upload")
def upload():
    # render upload page
    uid = uuid.uuid4().hex
    return render_template('upload.html',uid=uid)

@app.route('/completed')
def completed():
    uid = request.args.get('uid')
    return render_template('completed.html',uid=uid)

"""
object_name: name of the file.
expiry_time: denotes the expiry time of the URL.
"""
@app.route("/file-upload",methods=["GET"])
def file_upload():
    try:
        object_name = request.args.get('object_name')
    except:
        return jsonify({"message":"error: param `object_name` not specified!"})
    expiry_time = request.args.get('expiry_time',3600)

    fields=None
    conditions=None
    try:
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
    except:
        traceback.print_exc()
        error_dict = {"message":"unexpected error. traceback:"+traceback.format_exc()}
        return jsonify(error_dict)
    