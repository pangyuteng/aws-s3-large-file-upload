import os
import sys
import json
import time
from flask import Flask, jsonify, request
import boto3
from botocore.client import Config

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
settings_json_file = os.path.join(THIS_DIR,"zappa_setting.json")
with open(settings_json_file,"r") as f:
    content = json.loads(f.read())
    BUCKET_NAME = content["lambda_docker_flask"]["s3_bucket"]

app = Flask(__name__)

@app.route("/")
def serve():
    return jsonify(success=True)

@app.route("/time")
def get_current_time():
    return {"time": round(time.time())}

"""
object_name: name of the file.
expiry_time: denotes the expiry time of the URL.
"""
@app.route("/file-upload",methods=["GET"])
def file_upload():

    object_name = request.args.get('object_name')
    expiry_time = request.args.get('expiry_time',3600)

    fields=None
    conditions=None
    try:
        # The response contains the presigned URL and required fields
        client = boto3.client("s3",
            config=Config(signature_version="s3v4")
        )
        url = s3_client.generate_presigned_post(
            BUCKET_NAME,
            object_name,
            Fields=fields,
            Conditions=conditions,
            ExpiresIn=expiration,
        )
        return url
    except ClientError as e:
        logging.error(e)
        return None
    