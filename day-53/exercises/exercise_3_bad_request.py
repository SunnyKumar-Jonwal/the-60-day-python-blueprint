from fastapi import FastAPI, HTTPException

app = FastAPI()

# TODO: add POST /divide with query params a: float, b: float that raises
# HTTPException(400, "Cannot divide by zero") if b == 0, else returns
# {"result": a / b}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
