import json


def hello(event, context):
    body = {
        "message": "Hola.....12",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
