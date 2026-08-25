from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_users = {1: "Ada", 2: "Grace"}

# TODO: add GET /users/{user_id} (user_id: int) that:
# - raises HTTPException(403, "User is banned") if user_id == 0
# - raises HTTPException(404, "User not found") if user_id not in fake_users
# - otherwise returns {"user_id": user_id, "name": fake_users[user_id]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
