# FastAPI Template with MongoDB

This repository provides a FastAPI template with MongoDB setup using Docker Compose.

## Getting Started

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

### Start the services:

```
docker-compose up -d
```

### Verify the services:
```
docker-compose ps
 ```
### Stopping the Services
```
docker-compose down
 ```

### The database will be accessible on ```localhost:27017``` with the specified root username and password.

### Run App

[//]: # (uvicorn app.app:app --reload)

```
fastapi dev
```

```
 ╭────────── FastAPI CLI - Development mode ───────────╮                                                                                                                                                  
 │                                                     │                                                                                                                                                  
 │  Serving at: http://127.0.0.1:8000                  │                                                                                                                                                  
 │                                                     │                                                                                                                                                  
 │  API docs: http://127.0.0.1:8000/docs               │                                                                                                                                                  
 │                                                     │                                                                                                                                                  
 │  Running in development mode, for production use:   │                                                                                                                                                  
 │                                                     │                                                                                                                                                  
 │  fastapi run                                        │                                                                                                                                                  
 │                                                     │                                                                                                                                                  
 ╰─────────────────────────────────────────────────────╯ 
```

### Project Requirements

- Python 3.11
- FastAPI
- Mongodb
- Pydantic
- Pymongo
- Beanie