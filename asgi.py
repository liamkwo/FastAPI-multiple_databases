import uvicorn

from api.main import app

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=7777, reload=True)
