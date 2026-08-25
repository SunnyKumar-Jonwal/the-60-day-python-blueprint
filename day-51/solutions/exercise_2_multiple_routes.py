from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Home page"}


@app.get("/about")
def about():
    return {"message": "About this API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
