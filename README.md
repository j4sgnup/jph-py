# Django REST Framework API Example

This project demonstrates a Django REST Framework (DRF) API that fetches data from the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) external API, without using a local database.

## Features
- API endpoints for users, posts, and comments
- Service layer for external API calls
- Plain Python classes for data models
- DRF views and routing
- Logging for error handling

## Setup

### 1. Create and activate a virtual environment
```
python -m venv env
# Windows
env\Scripts\activate
# Git Bash
source env/Scripts/activate
```

### 2. Install dependencies
```
pip install django djangorestframework requests
```

### 3. Start a Django project and app
```
django-admin startproject api
cd api
python manage.py startapp posts
```

### 4. Project structure
```
api/
  api/
    settings.py
    urls.py
  posts/
    models.py
    views.py
    services.py
    urls.py
  manage.py
```

## Usage

1. Run the development server:
   ```
   python manage.py runserver
   ```
2. Access endpoints, e.g.:
   - `http://127.0.0.1:8000/api/users/`
   - `http://127.0.0.1:8000/api/posts/`
   - `http://127.0.0.1:8000/api/comments/`

## Notes
- Models are plain Python classes, not Django ORM models.
- Data is fetched from JSONPlaceholder, not a local database.
- Logging is configured in `settings.py`.

## License
MIT
