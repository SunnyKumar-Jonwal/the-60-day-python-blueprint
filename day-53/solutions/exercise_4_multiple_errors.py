from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_users = {1: "Ada", 2: "Grace"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id == 0:
        raise HTTPException(status_code=403, detail="User is banned")
    if user_id not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "name": fake_users[user_id]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
