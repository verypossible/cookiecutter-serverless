"""Template for a Python3 project on AWS."""
import json
import sys

from pathlib import Path

# pylint: disable=wrong-import-position

# Munge our sys path so libs can be found
LIB = Path(__file__).resolve().parent / 'lib'
sys.path.insert(0, str(LIB))


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
