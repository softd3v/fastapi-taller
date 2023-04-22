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