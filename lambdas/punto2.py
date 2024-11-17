import json


def hello(event, context):
    
    try:
        name = event["queryStringParameters"]["name"]
        body = {
            "message": f"hola {name}",
        }
    except:
        body = {
            "Error": f"El Parametro name es requerido (Es un query String Parameter)",
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
