from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from enum import IntEnum

class Priority(IntEnum):
    low = 1
    medium = 2
    high = 3

class AddedTask(BaseModel):
    name: str = Field(..., max_length=100, min_length=1)
    deadline: Optional[str] = None
    priority: Priority = Priority.medium

