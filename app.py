import time
from flask import Flask, jsonify
import boto3
from botocore.client import Config

app = Flask(__name__)

@app.route("/")
def serve():
    return jsonify(success=True)

@app.route("/time")
def get_current_time():
    return {"time": round(time.time())}

@app.route("/create-presigned-post")
def create_presigned_post():

    fields=None
    conditions=None
    expiration=3600
    try:
        # The response contains the presigned URL and required fields
        client = boto3.client("s3")
        response s3_client.generate_presigned_post(
            bucket_name,
            object_name,
            Fields=fields,
            Conditions=conditions,
            ExpiresIn=expiration,
        )
        return response
    except ClientError as e:
        logging.error(e)
        return None
    