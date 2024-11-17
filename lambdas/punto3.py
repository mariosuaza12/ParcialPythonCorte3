import json

def calculadora_lambda(event, context):
    try:
    
        params = event.get("queryStringParameters", {})
        
        
        if not params or not all(k in params for k in ("a", "b", "operador")):
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Todos los parámetros son obligatorios: 'a', 'b' y 'operador'.",
                    "ejemplo": "Debes enviar los parámetros como: ?a=10&b=5&operador=+"
                })
            }

        a = params.get("a")
        b = params.get("b")
        operador = params.get("operador")

        
        if operador == " " or operador.strip() == "":
            operador = "+"

       
        if not a.strip() or not b.strip() or not operador.strip():
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Ningún parámetro puede estar vacío. Verifica que 'a', 'b' y 'operador' contengan valores válidos.",
                    "ejemplo": "Debes enviar los parámetros como: ?a=10&b=5&operador=+"
                })
            }

       
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Los valores de 'a' y 'b' deben ser numéricos.",
                    "ejemplo": "Debes enviar los parámetros como: ?a=10&b=5&operador=+"
                })
            }

        
        if operador not in ["+", "-", "*", "/"]:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Operador no válido. Use '+', '-', '*', '/'.",
                    "ejemplo": "Debes enviar los parámetros como: ?a=10&b=5&operador=+"
                })
            }

        # Realizar la operación
        if operador == "+":
            resultado = a + b
        elif operador == "-":
            resultado = a - b
        elif operador == "*":
            resultado = a * b
        elif operador == "/":
            if b == 0:
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "error": "División por cero no permitida.",
                        "ejemplo": "Debes enviar los parámetros como: ?a=10&b=5&operador=/"
                    })
                }
            resultado = a / b

        # Devolver el resultado en JSON
        return {
            "statusCode": 200,
            "body": json.dumps({"resultado": resultado})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": f"Error interno del servidor: {str(e)}",
                "ejemplo": "Debes enviar los parámetros como: ?a=10&b=5&operador=+"
            })
        }
