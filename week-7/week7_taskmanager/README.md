# Week 7 – Task Manager (DRF + JavaScript Demo Project)

A live-coding demo project for the Week 7 lecture on REST APIs, Django REST Framework, and JavaScript.

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Apply migrations
python manage.py migrate

# 3. (Optional) Seed sample tasks
python manage.py shell -c "
from tasks.models import Task
Task.objects.create(title='Learn DRF', priority='high', completed=True)
Task.objects.create(title='Build the API', priority='high')
Task.objects.create(title='Add JavaScript frontend', priority='medium')
"

# 4. Create superuser for admin panel
python manage.py createsuperuser

# 5. Run server
python manage.py runserver
```

Visit **http://127.0.0.1:8000** to see the JavaScript frontend.

---

## Lecture Demo Flow

| Day | URL to show | What to demonstrate |
|-----|-------------|---------------------|
| 1 | `/api/tasks-json/` | Manual `JsonResponse` — shows why DRF is needed |
| 2 | `/api/v1/tasks/` | `@api_view` + DRF Browsable API |
| 2 | `/api/v1/tasks/1/` | Single task with GET / PUT / DELETE |
| 3 | `/api/tasks/` | ViewSet + Router (same result, 5 lines of code) |
| 3 | `/api/tasks/stats/` | Custom `@action` (collection) |
| 3 | `/api/tasks/1/toggle/` | Custom `@action` (detail) |
| 4/5 | `/` | JavaScript frontend consuming the API |
| Any | `/admin/` | Admin panel for live data editing |

---

## Project Structure

```
week7_taskmanager/
├── manage.py
├── requirements.txt
├── week7_taskmanager/       ← Django project (settings, urls)
│   ├── settings.py          ← REST_FRAMEWORK config + INSTALLED_APPS
│   └── urls.py              ← includes tasks.urls + api-auth/
├── tasks/                   ← Main app
│   ├── models.py            ← Task model (title, completed, priority)
│   ├── serializers.py       ← TaskSerializerBasic + TaskSerializer (ModelSerializer)
│   ├── views.py             ← Day1: JsonResponse, Day2: @api_view, Day3: ViewSet
│   ├── urls.py              ← Router + all URL patterns
│   └── admin.py             ← TaskAdmin with list_editable
└── templates/
    ├── base.html            ← Navbar, API explorer bar, getCookie(), showFlash()
    └── home.html            ← Stats dashboard + create form + task list (JS SPA)
```

---

## API Endpoints Summary

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create task |
| GET | `/api/tasks/<id>/` | Get one task |
| PUT | `/api/tasks/<id>/` | Full update |
| PATCH | `/api/tasks/<id>/` | Partial update |
| DELETE | `/api/tasks/<id>/` | Delete task |
| POST | `/api/tasks/<id>/toggle/` | Toggle completed ✓ |
| GET | `/api/tasks/stats/` | Dashboard stats ✓ |
| POST | `/api/tasks/clear-completed/` | Bulk delete ✓ |
| GET | `/api/tasks/?completed=true` | Filter by status |
| GET | `/api/tasks/?priority=high` | Filter by priority |

> ✓ = custom `@action` (shown on Day 3)

---

## Demo Credentials

- Admin: `admin` / `admin123`
- Browsable API login: `/api-auth/login/`
