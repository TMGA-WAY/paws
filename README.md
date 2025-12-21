# paws

#### Directory structure

1. base directory - ```snoot```
2. api routers - ```snoot\routers``` - To handle API endpoints
3. schema - ```snoot\schema``` - To define input validation and output serialization
4. models - ```snoot\models``` - To define database models
5. database - ```snoot\database``` - To handle database connections, sessions and utility function for CRUD operations
6. security - ```snoot\security``` - To handle authentication, authorization, password hashing and token generation
7. utils - ```snoot\notifications``` - To handle email, mobile notifications and other utility functions
8. scheduled tasks - ```snoot\tasks``` - To handle background jobs and scheduled tasks
9. services - ```snoot\services``` - To handle external services integration like payment gateways, third-party APIs
   etc.
10. design_patterns - ```snoot\services\*``` - To implement common design patterns like Singleton, Factory, Observer
    etc.


# Project setup

start server in development mode:
```console
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```


Db-migrations:
```console
alembic revision --autogenerate -m "commit message"
alembic upgrade head
```