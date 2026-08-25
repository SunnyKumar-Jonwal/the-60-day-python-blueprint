from fastapi import FastAPI, HTTPException, status

app = FastAPI()

fake_items = {1: "Widget", 2: "Gadget"}


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item():
    return {"message": "Item created"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in fake_items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": fake_items[item_id]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
