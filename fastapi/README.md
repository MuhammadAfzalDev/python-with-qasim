# FastAPI Project

A modern FastAPI project with a well-organized structure and best practices.

## Features

- FastAPI framework with async support
- SQLAlchemy for database operations
- Alembic for database migrations
- Pydantic for data validation
- JWT authentication
- Environment variable management
- Testing setup with pytest

## Project Structure

```
fastapi/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   └── router.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── db/
│   │   │   └── base.py
│   │   ├── models/
│   │   │   └── user.py
│   │   └── schemas/
│   │       └── user.py
│   ├── tests/
│   │   └── test_api/
│   ├── alembic/
│   ├── .env
│   ├── main.py
│   └── requirements.txt
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your environment variables:
```
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI): http://localhost:8000/docs
- Alternative API documentation (ReDoc): http://localhost:8000/redoc

## Testing

Run tests with pytest:
```bash
pytest
``` 