from fastapi import FastAPI

app = FastAPI()


@app.get("/products")
def list_products(category: str, page: int = 1):
    return {"category": category, "page": page}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
