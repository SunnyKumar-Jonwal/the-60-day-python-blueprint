from fastapi import FastAPI
from routers.books import repository
from routers.books import router as books_router

BOOKS_CSV = "day-59/project/books.csv"

repository.load_from_csv(BOOKS_CSV)

app = FastAPI(title="Library API")
app.include_router(books_router)


@app.get("/")
def read_root():
    return {"message": "Library API -- see /docs for available endpoints"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
