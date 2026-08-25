from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    username: str


# TODO: add POST /users that receives a UserIn, uses response_model=UserOut,
# and returns the received user (the password should be excluded from the response)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
