from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.router import chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # especifique em prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)

# Serve frontend da pasta /static
app.mount("/", StaticFiles(directory="static", html=True), name="static")
