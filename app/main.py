from fastapi import FastAPI
from pydantic import BaseModel 
from uuid import uuid4
from enum import Enum
from app.services.vm_service import create_vm_service
from app.api.vm import router as vm_router

app = FastAPI(title = "VM Lifecycle API")
app.include_router(vm_router)

