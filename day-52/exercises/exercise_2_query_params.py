from fastapi import FastAPI

app = FastAPI()

# TODO: add GET /products with query params category: str (required) and
# page: int = 1 (optional), returning {"category": category, "page": page}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
