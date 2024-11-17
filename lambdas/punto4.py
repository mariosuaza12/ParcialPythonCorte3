import json

def procesamiento_texto_lambda(event, context):
    try:
        # Obtener el cuerpo de la solicitud
        body = event.get("body", None)
        
        # Validar que el cuerpo no esté vacío
        if not body:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "El cuerpo de la solicitud está vacío. Debes enviar un texto en formato JSON.",
                    "ejemplo": {
                        "texto": "Este es un ejemplo de texto"
                    }
                })
            }
        
        # Parsear el JSON del cuerpo
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "El cuerpo de la solicitud no tiene un formato JSON válido.",
                    "ejemplo": {
                        "texto": "Este es un ejemplo de texto"
                    }
                })
            }
        
        # Validar que el texto exista en el JSON
        texto = data.get("texto", None)
        if not texto:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "El campo 'texto' es obligatorio.",
                    "ejemplo": {
                        "texto": "Este es un ejemplo de texto"
                    }
                })
            }
        
        # Procesar el texto
        texto_mayusculas = texto.upper()
        palabras = len(texto.split())
        caracteres = len(texto)
        
        # Construir la respuesta
        respuesta = {
            "palabras": palabras,
            "caracteres": caracteres,
            "texto_mayusculas": texto_mayusculas
        }
        
        return {
            "statusCode": 200,
            "body": json.dumps(respuesta)
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": f"Error interno del servidor: {str(e)}"
            })
        }
