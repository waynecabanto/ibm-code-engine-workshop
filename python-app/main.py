from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    # Get the environment variable APP_MESSAGE
    message = os.getenv("APP_MESSAGE", "Default Message")
    return {"message": message}
