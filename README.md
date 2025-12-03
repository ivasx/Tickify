# Tickify - Task Management System

[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![DRF](https://img.shields.io/badge/DRF-3.14-red.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A feature-rich task management web application built with Django and Django REST Framework. Tickify helps users organize their tasks efficiently with categories, priorities, deadlines, and a clean, intuitive interface.

## Features

### Core Functionality
- **Task Management**: Create, read, update, and delete tasks with ease
- **Category Organization**: Group tasks into custom categories for better organization
- **Priority System**: 5-level priority system (Default, Low, Medium, High, Critical)
- **Status Tracking**: Mark tasks as completed or active
- **Deadline Management**: Set and track task deadlines
- **Photo Attachments**: Add images to tasks for visual context

### User Features
- **User Authentication**: Secure registration and login system
- **Email Authentication**: Support for both username and email login
- **Password Recovery**: Email-based password reset functionality
- **User Profiles**: Customizable user profiles with personal information
- **Permission System**: Role-based access control for admin features

### API Features
- **RESTful API**: Complete REST API for all task operations
- **Token Authentication**: Secure API access using DRF token authentication
- **API Documentation**: Browsable API interface with DRF
- **Djoser Integration**: Extended user authentication endpoints

### UI/UX
- **Responsive Design**: Mobile-friendly interface
- **Dark Theme Ready**: CSS infrastructure for dark theme support
- **Pagination**: Efficient handling of large task lists
- **Filtering**: Filter tasks by category and completion status
- **Search**: Quick task search functionality
- **Custom Admin Panel**: Enhanced Django admin interface

## Technology Stack

**Backend:**
- Django 4.2
- Django REST Framework
- Djoser (authentication)
- Python Slugify

**Frontend:**
- HTML5/CSS3
- Vanilla JavaScript
- Responsive CSS Grid/Flexbox

**Database:**
- SQLite (development)
- PostgreSQL ready (production)

**Additional Tools:**
- Django Debug Toolbar
- Django Extensions

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/tickify.git
cd tickify
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## Configuration

### Email Settings
Configure SMTP settings in `tickify/settings.py`:
```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
EMAIL_USE_SSL = True
```

### Static and Media Files
```python
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## API Documentation

### Authentication Endpoints
```
POST /auth/users/                    # Register new user
POST /auth/token/login/              # Obtain auth token
POST /auth/token/logout/             # Logout user
```

### Task Endpoints
```
GET    /api/v1/tasks/                # List all tasks
POST   /api/v1/tasks/                # Create new task
GET    /api/v1/tasks/{slug}/         # Retrieve task details
PUT    /api/v1/tasks/{slug}/         # Update task
DELETE /api/v1/tasks/{slug}/         # Delete task
GET    /api/v1/tasks/category/{id}/  # Get tasks by category
```

### Example API Request
```bash
curl -X POST http://127.0.0.1:8000/api/v1/tasks/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Task",
    "description": "Task description",
    "priority": 2,
    "deadline": "2024-12-31T23:59:59Z"
  }'
```

## Project Structure

```
tickify/
├── manage.py
├── tickify/                 # Main project directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/                   # Tasks app
│   ├── models.py           # Task and Category models
│   ├── views.py            # Views and ViewSets
│   ├── serializers.py      # DRF serializers
│   ├── forms.py            # Django forms
│   ├── admin.py            # Admin customization
│   └── templates/          # HTML templates
├── users/                   # Users app
│   ├── models.py           # Custom user model
│   ├── views.py            # Authentication views
│   ├── forms.py            # User forms
│   └── templates/          # User templates
├── static/                  # Static files (CSS, JS)
└── media/                   # User uploaded files
```

## Key Models

### Task Model
- `title`: Task title (CharField)
- `slug`: URL-friendly identifier (SlugField)
- `description`: Task details (TextField)
- `completed`: Task status (BooleanField)
- `priority`: Priority level (IntegerField)
- `deadline`: Task deadline (DateTimeField)
- `category`: Related category (ForeignKey)
- `user`: Task owner (ForeignKey)
- `photo`: Task image (ImageField)

### Category Model
- `name`: Category name (CharField)
- `slug`: URL-friendly identifier (SlugField)
- `user`: Category owner (ForeignKey)

## Security Features

- CSRF protection enabled
- SQL injection prevention through ORM
- XSS protection with Django templates
- Secure password hashing
- Token-based API authentication
- Permission-based access control

## Testing

Run tests with:
```bash
python manage.py test
```

## Development Notes

### Custom Managers
- `CompletedManager`: Filter completed tasks
- `UncompletedManager`: Filter active tasks

### Custom Permissions
- `IsOwner`: Ensures users can only access their own tasks
- Admin-specific views require `change_user` permission

### Form Validation
- Category ownership validation
- Unique category names per user
- Title length validation
- Email uniqueness validation

## Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up PostgreSQL database
- [ ] Configure static file serving
- [ ] Set up media file storage
- [ ] Configure email backend
- [ ] Set strong `SECRET_KEY`
- [ ] Enable HTTPS
- [ ] Configure CORS if needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**ivasx**

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/tickify/issues).

## Show your support

Give a star if this project helped you!

---

**Note**: This is a portfolio project demonstrating Django and DRF skills. For production use, additional security measures and optimizations should be implemented.