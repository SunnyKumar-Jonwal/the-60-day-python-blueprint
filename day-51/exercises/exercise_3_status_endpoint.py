from fastapi import FastAPI

app = FastAPI()

# TODO: add a GET /health endpoint returning {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
