from fastapi import FastAPI
from routers.notes import router as notes_router

app = FastAPI()
app.include_router(notes_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
