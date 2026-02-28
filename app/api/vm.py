from fastapi import APIRouter, HTTPException
from app.models.vm import VMRequest
from app.services.vm_service import *

router = APIRouter(prefix = "/vms", tags=["VMs"])

@router.post("/")
def create_vm(request: VMRequest):
    return create_vm_service(request)

    
@router.post("/{vm_id}/start")
def start_vm(vm_id: str):
    result = start_vm_service(vm_id)
    if result is None:
        raise HTTPException(404, "VM not found")
    if result == "already_running":
        raise HTTPException(400, "VM already running")
    return result

@router.post("/{vm_id}/stop")
def stop_vm(vm_id: str):
    result = stop_vm_service(vm_id)
    if result is None:
        raise HTTPException(404, "VM not found")
    if result == "already_stopped":
        raise HTTPException(400, "VM already stopped")
    return result

@router.delete("/{vm_id}")
def delete_vm(vm_id: str):
    result = delete_vm_service(vm_id)
    if result is None:
        raise HTTPException(404, "VM not found")
    return {"message": "VM deleted"}


