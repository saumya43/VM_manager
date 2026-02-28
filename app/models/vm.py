from pydantic import BaseModel
from enum import Enum
from uuid import uuid4

class VMRequest(BaseModel):
    name: str

class VMStatus(str, Enum):
    RUNNING = "running"
    STOPPED = "stopped"

class VM(BaseModel):
    id: str
    name: str
    status: VMStatus
  