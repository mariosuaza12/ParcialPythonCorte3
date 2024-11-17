import boto3
import json


def consultar_estudiante(event, context):
    try:
        # Obtener el ID desde los parámetros de la URL
        params = event.get("queryStringParameters", {})
        estudiante_id = params.get("id") if params else None

        if not estudiante_id:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "El parámetro 'id' es obligatorio. Ejemplo: ?id=123"
                })
            }

        # Configurar la conexión a DynamoDB
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("Estudiantes")

        # Consultar por el ID
        response = table.get_item(Key={"id": estudiante_id})

        # Verificar si el estudiante existe
        if "Item" not in response:
            return {
                "statusCode": 404,
                "body": json.dumps({
                    "error": f"No se encontro un estudiante con id: {estudiante_id}"
                })
            }

        # Retornar los datos del estudiante
        estudiante = response["Item"]
        return {
            "statusCode": 200,
            "body": json.dumps(estudiante)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Error interno del servidor.",
                "detalles": str(e)
            })
        }
