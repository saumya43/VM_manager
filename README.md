#  VM Lifecycle Management API

##  Project Overview

This project implements a VM lifecycle management system. It provides REST APIs to create, start, stop, retrieve, and delete virtual machines.

The system is built using FastAPI and follows a layered architecture to separate API handling, business logic, and storage. It serves as a proof-of-concept demonstrating backend engineering, API design, and system design principles.

---

##  Features

* Create VM
* List all VMs
* Start VM
* Stop VM
* Delete VM
* Input validation using Pydantic
* Layered architecture (API, Service, Storage)

---

##  Architecture

```
Client → API Layer → Service Layer → Storage Layer
```

###  API Layer

Handles HTTP requests and responses, validates input using Pydantic, and maps service outputs to appropriate HTTP status codes.

###  Service Layer

Encapsulates business logic for VM lifecycle management, including state transitions and validation of operations.

###  Storage Layer

Uses an in-memory dictionary to store VM data. This is suitable for a prototype but does not persist data across restarts.

---

##  API Endpoints

### Create VM

POST /vms

Request:
```json
{
  "name": "vm1"
}
```

### List VMs

GET /vms

### Get VM

GET /vms/{vm_id}

### Start VM

POST /vms/{vm_id}/start

### Stop VM

POST /vms/{vm_id}/stop

### Delete VM

DELETE /vms/{vm_id}

---

##  Setup Instructions

1. Clone the repository

2. Create virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate environment:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Access API docs:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## Design Decisions

### Use of Pydantic

Used for input validation and structured data handling, reducing manual validation and improving API clarity.

### In-Memory Storage

Chosen for simplicity and rapid prototyping. Not suitable for production due to lack of persistence.

### Layered Architecture

Separates API, business logic, and storage to improve maintainability, testability, and reusability.

---

##  Roadmap / Future Enhancements

* Replace in-memory storage with Database
* Add asynchronous task processing for VM operations
* Introduce message queue for scalability
* Implement logging and monitoring
* Add authentication and authorization
* Containerize using Docker and deploy on Kubernetes

---

##  Limitations

* No persistent storage
* No authentication
* Synchronous execution of operations
* Not production-ready (prototype only)


