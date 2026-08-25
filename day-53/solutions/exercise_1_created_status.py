from fastapi import FastAPI, status

app = FastAPI()


@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note():
    return {"message": "Note created"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
