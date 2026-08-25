from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

tasks = {}
next_id = 1


class Task(BaseModel):
    title: str


@app.post("/tasks", status_code=201)
def create_task(task: Task):
    global next_id
    task_id = next_id
    tasks[task_id] = task.title
    next_id += 1
    return {"id": task_id, "title": task.title}


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": task_id, "title": tasks[task_id]}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task.title
    return {"id": task_id, "title": task.title}


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return Response(status_code=204)
