from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uvicorn

# Inicjalizacja aplikacji FastAPI
app = FastAPI(title="Todo API", description="Prosta aplikacja do zarządzania zadaniami")

# Model danych dla zadania
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False
    created_at: datetime = datetime.now()

# Symulacja bazy danych (w pamięci)
tasks_db = {}
task_counter = 1

# Endpointy API

@app.get("/")
async def root():
    """Strona główna API"""
    return {"message": "Witaj w Todo API!"}

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """Pobierz wszystkie zadania"""
    return list(tasks_db.values())

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Pobierz pojedyncze zadanie po ID"""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Zadanie nie zostało znalezione")
    return tasks_db[task_id]

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    """Utwórz nowe zadanie"""
    global task_counter
    task.id = task_counter
    tasks_db[task_counter] = task
    task_counter += 1
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    """Zaktualizuj istniejące zadanie"""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Zadanie nie zostało znalezione")
    task.id = task_id
    tasks_db[task_id] = task
    return task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Usuń zadanie"""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Zadanie nie zostało znalezione")
    del tasks_db[task_id]
    return {"message": "Zadanie zostało usunięte"}

@app.patch("/tasks/{task_id}/complete")
async def complete_task(task_id: int):
    """Oznacz zadanie jako wykonane"""
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Zadanie nie zostało znalezione")
    tasks_db[task_id].completed = True
    return {"message": "Zadanie zostało oznaczone jako wykonane"}

if __name__ == "__main__":
    uvicorn.run("fastapi_app:app", host="0.0.0.0", port=8000, reload=True) 