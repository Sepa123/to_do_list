from fastapi import FastAPI
from routers import todo_list

app = FastAPI()

app.include_router(todo_list.router)

## iniciar servicio: uvicorn main:app --reload
## doc http://127.0.0.1:8000/docs
## doc http://127.0.0.1:8000/redoc

@app.get("/")
async def hola():
    return {
        "message":"hola mundo"
    }