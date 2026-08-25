from fastapi import FastAPI

app = FastAPI()

# TODO: add GET /users/{user_id} (user_id: int) returning {"user_id": user_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
