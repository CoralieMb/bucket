from flask import Flask, render_template, request, redirect
import boto3

app = Flask(__name__)
s3 = boto3.resource('s3')

# get an item from a given bucket
@app.route("/get_item/<bucket>/<item_name>", methods=['GET'])
def get_item_in_bucket(item_name, bucket):
    if request.method == 'GET':
        if item_name:
            response = s3.get_object(
                    Bucket=bucket,
                    Key=item_name
            )
            return response

