"""Template for a Python3 project on AWS."""
import json
import sys

# pylint: disable=wrong-import-position

# Update our sys path libs stored in our Layer can be found. All imports for additional libraries
# should come *after* this line.
sys.path.insert(0, '/opt')


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
    }

    return response
