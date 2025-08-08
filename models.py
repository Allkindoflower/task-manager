from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class AddedTask(BaseModel):
    name: str
    deadline: Optional[str] = None
    priority: Priority = Priority.MEDIUM