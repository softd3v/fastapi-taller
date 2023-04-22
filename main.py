from fastapi import FastAPI

app = FastAPI()

@app.get('/main')
async def main():
    return "SALUDOS!! LLEGAMOS AQUI Y AHORA QUE?"

@app.get('/empleado')
async def empleado():
    return {"id": "EST3478",
            "nombre": "Jhon",
            "apellido": "Doe",
            "edad": "27",
            "email": "j.doe@panama.com"
           }

@app.get('/curso')
async def curso():
    return {"id": "CR09878",
            "nombre": "CURSO PYTHON",
            "facilitador": "JHON DOE",
            "horas": "5"
           }
