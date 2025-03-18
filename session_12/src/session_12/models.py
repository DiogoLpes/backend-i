
from datetime import datetime 
from sqlmodel import Field, SQLModel
from typing import Optional


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    due_date: datetime
    is_done: bool = False