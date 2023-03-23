from fastapi import APIRouter, HTTPException, status
from database.models.task import Task
from database.schemas.task import task_schema, tasks_schema
from database.client import db_client
from datetime import datetime
from bson import ObjectId # para la id de mongodb

router = APIRouter(tags=["todo_list"],prefix="/todo")

def is_found(found):
    if not found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
    
def search_task(field:str, key):
    try:
        task = task_schema(db_client.tasks.find_one({field : key}))
        return Task(**task)
    except:
        return {"error":"error con la busqueda de tarea"}
    
@router.get("/")
async def get_tasks():
    return tasks_schema(db_client.tasks.find())

@router.get("/{id}")
async def get_task(id: str):
    found_task = search_task("_id", ObjectId(id))
    return found_task

@router.post("/",status_code= status.HTTP_201_CREATED, response_model=Task)
async def add_task( task : Task):
    task_dict = dict(task)
    del task_dict["id"]
    task_dict["is_completed"] = False
    task_dict["creation_date"] = datetime.now()
    
    id = db_client.tasks.insert_one(task_dict).inserted_id

    new_task = task_schema(db_client.tasks.find_one({"_id": id}))

    return Task(**new_task)

@router.delete("/{id}",status_code=status.HTTP_202_ACCEPTED)
async def delete_task(id: str):
    found = db_client.tasks.find_one_and_delete({"_id": ObjectId(id)})

    is_found(found)
    
    return {"message": "Tarea eliminada"}
@router.put("/",status_code=status.HTTP_202_ACCEPTED)
async def update_task(task: Task):
    try:
        task_dict = dict(task)
        del task_dict["id"], task_dict["creation_date"], task_dict["expiration_date"]
        task_dict["update_date"] = datetime.now()

        found = db_client.tasks.find_one_and_update({"_id": ObjectId(task.id)}, {"$set": task_dict})
        # El operador $set permite actualizar solo algunos datos del documento
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se ha podido actualizar") 
    
    is_found(found)
    
    return {"message": "Tarea actualizada"}
    
