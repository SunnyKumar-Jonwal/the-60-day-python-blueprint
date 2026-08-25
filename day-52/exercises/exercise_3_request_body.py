from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# TODO: define a Task model with title: str and done: bool = False
# TODO: add POST /tasks that receives a Task and returns it


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
