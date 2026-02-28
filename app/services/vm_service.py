from uuid import uuid4
from app.models.vm import VM, VMStatus
from app.core.storage import vm_db

def create_vm_service(request):
    vm = VM(
        id=str(uuid4()),
        name=request.name,
        status=VMStatus.RUNNING
    )
    return vm

def start_vm_service(vm_id):
    vm = vm_db.get(vm_id)
    if not vm:
        return None

    if vm.status == VMStatus.RUNNING:
        return "already_running"

    vm.status = VMStatus.RUNNING
    return vm


def stop_vm_service(vm_id):
    vm = vm_db.get(vm_id)
    if not vm:
        return None

    if vm.status == VMStatus.STOPPED:
        return "already_stopped"

    vm.status = VMStatus.STOPPED
    return vm
   
def delete_vm_service(vm_id):
    vm = vm_db.get(vm_id)
    if not vm:
        return None
    
    vm_db.pop(vm_id)
    return vm
    