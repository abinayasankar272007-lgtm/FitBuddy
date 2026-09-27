from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
import os

app = FastAPI()

# Output folder create pannu
os.makedirs("output", exist_ok=True)

# Static folders mount pannu - ithu than PDF ku mukkiyam da!
app.mount("/output", StaticFiles(directory="output"), name="output")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)