import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/random")
def get_random():
    return {"number": random.randint(1, 100)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
