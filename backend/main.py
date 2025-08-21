"""FastAPI application exposing health and task endpoints."""
from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="CodePro Mark1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    """Simple in-memory task representation."""
    id: int
    text: str

_tasks: list[Task] = []

@app.get("/health")
async def health() -> dict[str, bool]:
    """Health check endpoint."""
    return {"ok": True}

@app.get("/tasks", response_model=list[Task])
async def list_tasks() -> list[Task]:
    return _tasks

@app.post("/tasks", response_model=Task)
async def create_task(task: Task) -> Task:
    if any(t.id == task.id for t in _tasks):
        raise HTTPException(status_code=400, detail="id exists")
    _tasks.append(task)
    return task
