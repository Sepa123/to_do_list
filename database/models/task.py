from pydantic import BaseModel
from datetime import datetime

class Task(BaseModel):
    id : str | None
    task: str
    type_task:str
    is_completed: bool | None
    creation_date: datetime | None
    expiration_date: datetime | None
    update_date: datetime | None
    # user : str
    
