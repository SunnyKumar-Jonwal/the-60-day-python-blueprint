from fastapi import FastAPI
from routers.books import router as books_router

app = FastAPI()
app.include_router(books_router)


@app.get("/")
def read_root():
    return {"message": "Books API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
