from fastapi import FastAPI
from api import research
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles



app = FastAPI(
    title="AI Company Research Assistant API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-company-research-assistant-bxbl.vercel.app/"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
from fastapi.staticfiles import StaticFiles

os.makedirs("reports", exist_ok=True)

app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports"
)

app.include_router(
    research.router,
    prefix="/research"
)


@app.get("/")
def home():

    return {
        "message": "AI Research Backend Running"
    }
