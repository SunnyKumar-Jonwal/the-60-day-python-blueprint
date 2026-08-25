from fastapi import FastAPI

app = FastAPI()

# TODO: add a GET / endpoint that returns {"message": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
