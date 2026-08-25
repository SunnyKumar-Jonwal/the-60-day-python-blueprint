from fastapi import FastAPI

app = FastAPI()

# TODO: add GET / returning {"message": "Home page"}
# TODO: add GET /about returning {"message": "About this API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
