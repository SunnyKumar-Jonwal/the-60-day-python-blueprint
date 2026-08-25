from fastapi import FastAPI, status

app = FastAPI()

# TODO: add POST /notes with status_code=status.HTTP_201_CREATED, returning
# {"message": "Note created"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
