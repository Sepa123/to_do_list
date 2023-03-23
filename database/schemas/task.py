def task_schema(task) -> dict:
    return {
    "id": str(task["_id"]),
    "task": task["task"],
    "type_task": task["type_task"],
    "is_completed": task["is_completed"],
    "creation_date": task["creation_date"],
    "expiration_date": task["expiration_date"],
    "update_date": task["update_date"]
  }

def tasks_schema(tasks) -> list:
    return [task_schema(task) for task in tasks] 