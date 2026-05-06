import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Incident Management System",
    version="1.0.0",
    description="Mission-Critical Incident Management System for Zeotap as part of the internship assignment."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(incidents_router)

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "app": "Incident Management System",
        "version": "1.0.0"
    }
