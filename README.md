# CareerHub

CareerHub is a Django-based Job & Internship Portal built as a practical Django/backend portfolio project.

## Features

### Student Features

- Student registration
- Student login/logout
- Student dashboard
- Student profile
- Edit student profile
- Profile image upload
- Resume upload
- Browse jobs
- Search jobs
- Filter jobs by location and job type
- View complete job details
- Apply for jobs
- View submitted applications
- Track application status

### Company Features

- Company registration
- Company login/logout
- Company dashboard
- Company profile
- Edit company profile
- Company logo upload
- Post jobs and internships
- View own posted jobs
- Edit jobs
- Delete jobs
- View applicants
- View applicant education, skills and location
- View applicant resume
- Update application status

### Admin Features

- Django Admin
- Custom CareerHub Admin Dashboard
- View total students
- View total companies
- View total jobs
- View total applications
- Manage project data through Django Admin

---

## Technology Stack

- Python
- Django 6.1.1
- SQLite
- HTML
- Bootstrap 5
- Django Templates
- Git
- GitHub

---

## Project Structure

Careerhub/
│
├── careerhub/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   └── views.py
│
├── media/
│   ├── profile_images/
│   ├── resumes/
│   └── company_logos/
│
├── manage.py
├── .gitignore
└── db.sqlite3

---

## Database Models

### StudentProfile

StudentProfile stores additional information about a student.

Fields include:

- User
- Phone
- Profile Image
- Education
- Skills
- Resume
- Location
- Bio

StudentProfile has a One-to-One relationship with Django's built-in User model.

### CompanyProfile

CompanyProfile stores company information.

Fields include:

- User
- Company Name
- Logo
- Website
- Location
- Description

CompanyProfile also has a One-to-One relationship with Django's User model.

### Job

Job stores job and internship information.

Fields include:

- Company
- Title
- Description
- Location
- Salary
- Job Type
- Skills Required
- Created At
- Last Date

A company can create multiple jobs.

### Application

Application connects a student with a job.

Fields include:

- Student
- Job
- Applied At
- Status

Default status:

Pending

Other statuses:

- Shortlisted
- Rejected

A unique constraint prevents the same student from applying to the same job more than once.

---

## Database Relationships

User → StudentProfile

One User can have one StudentProfile.

User → CompanyProfile

One User can have one CompanyProfile.

CompanyProfile → Job

One Company can have multiple Jobs.

StudentProfile → Application

One Student can have multiple Applications.

Job → Application

One Job can have multiple Applications.

---

## Student Workflow

Register

↓

Student Login

↓

Student Dashboard

↓

Complete Profile

↓

Upload Resume

↓

Browse Jobs

↓

View Job Details

↓

Apply for Job

↓

My Applications

↓

Track Application Status

---

## Company Workflow

Register Company

↓

Company Login

↓

Company Dashboard

↓

Complete Company Profile

↓

Post Job

↓

My Jobs

↓

View Applicants

↓

View Applicant Resume

↓

Update Application Status

---

## Authentication

CareerHub uses Django's built-in authentication system.

Important functions used:

- authenticate()
- login()
- logout()

Protected views use:

@login_required

Role-based checks are also implemented so that students and companies can access only the functionality related to their role.

---

## Student Features

Students can create an account and log in to CareerHub.

After login, students can:

- Open Student Dashboard
- Create/update their profile
- Upload profile image
- Upload resume
- Browse jobs
- Search jobs
- Filter jobs
- View job details
- Apply for jobs
- View their applications
- Track application status

---

## Company Features

Companies can create an account and log in to CareerHub.

After login, companies can:

- Open Company Dashboard
- Create/update company profile
- Upload company logo
- Post jobs
- View their jobs
- Edit jobs
- Delete jobs
- View applicants
- View applicant resume
- Update application status

---

## Job Search

The job listing page supports:

- Job title search
- Location filter
- Job type filter

Django ORM is used for filtering.

Examples:

title__icontains

location__icontains

job_type__icontains

---

## Job Application System

When a student applies for a job:

1. The logged-in user is checked.
2. The StudentProfile is retrieved.
3. The selected Job is retrieved.
4. An Application is created.
5. Application status starts as Pending.
6. The application appears in My Applications.
7. The company can view the applicant.
8. The company can update the application status.

---

## Application Status

The current application statuses are:

- Pending
- Shortlisted
- Rejected

Students can see the updated status from their My Applications page.

---

## File Uploads

Students can upload:

- Profile image
- Resume

Companies can upload:

- Company logo

Media configuration:

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

---

## Django Forms

Django Forms and ModelForms are used for important operations.

Forms used include:

- Student Registration Form
- Company Registration Form
- Job Form
- Student Profile Form
- Company Profile Form

Django forms provide:

- Validation
- Error handling
- Clean POST data
- Reusable form logic
- Database integration through ModelForms

---

## Important Django Concepts Used

The project covers many important Django concepts:

- Django Models
- Django ORM
- OneToOneField
- ForeignKey
- ModelForm
- UserCreationForm
- Authentication
- Authorization
- CRUD operations
- File uploads
- GET requests
- POST requests
- URL routing
- Django Templates
- Django Admin
- Database constraints
- Sessions
- Login protection

---

## Important Django Functions

render()

Used to return an HTML template.

redirect()

Used to redirect the user to another URL.

get_object_or_404()

Used to get an object or return a 404 error if the object does not exist.

authenticate()

Used to verify username and password.

login()

Used to log a user into the Django session.

logout()

Used to log the current user out.

---

## Django Template Concepts

The project uses Django Template Language.

Variables:

{{ variable }}

Conditions:

{% if condition %}
{% endif %}

Loops:

{% for item in items %}
{% endfor %}

URL reversing:

{% url 'url_name' %}

Template inheritance:

{% extends "core/base.html" %}

Content blocks:

{% block content %}
{% endblock %}

---

## Main URLs

/

create_job/

register_company/

company_login/

jobs/

jobs/<job_id>/

register_student/

student_login/

student_profile/

edit_student_profile/

apply_job/<job_id>/

my_application/

job_applicants/<job_id>/

my-jobs/

logout/

company_profile/

edit_company_profile/

update-application-status/<application_id>/

student_dashboard/

company_dashboard/

edit-job/<job_id>/

delete-job/<job_id>/

admin-dashboard/

admin/

---

## Django Admin

Django Admin is available at:

/admin/

The following models are registered:

- StudentProfile
- CompanyProfile
- Job
- Application

A separate custom CareerHub admin dashboard is available at:

/admin-dashboard/

The custom dashboard displays:

- Total Students
- Total Companies
- Total Jobs
- Total Applications

---

## Bootstrap UI

Bootstrap 5 is used to create the user interface.

Bootstrap is used for:

- Navbar
- Buttons
- Cards
- Forms
- Grid system
- Spacing
- Responsive design
- Mobile navigation

The project uses a common base template:

core/base.html

This allows common navigation and Bootstrap resources to be reused across pages.

---

## Git & GitHub

A .gitignore file is used to prevent unnecessary files from being uploaded to GitHub.

Important entries:

venv/

__pycache__/

*.pyc

db.sqlite3

media/

.env

This prevents:

- Virtual environment files
- Python cache files
- Local database
- Uploaded media
- Environment variables

from being committed.

---

## Useful Django Commands

Create migrations:

python manage.py makemigrations

Apply migrations:

python manage.py migrate

Run development server:

python manage.py runserver

Create superuser:

python manage.py createsuperuser

---

## Current Project Status

The core CareerHub functionality has been completed.

Implemented features include:

- Student registration
- Student login
- Student logout
- Company registration
- Company login
- Company logout
- Student dashboard
- Company dashboard
- Student profile
- Company profile
- Profile editing
- File uploads
- Job creation
- Job listing
- Job search
- Job filtering
- Job details
- Job applications
- Application tracking
- Applicant management
- Application status updates
- Job editing
- Job deletion
- Custom admin dashboard
- Django Admin
- Bootstrap UI
- Git configuration

---

## Future Improvements

Possible future improvements include:

- Forgot password
- Email password reset
- Pagination
- Better duplicate application handling
- Application deadline enforcement
- Skills-based search
- Job categories
- Saved/bookmarked jobs
- Email notifications
- Company verification
- Profile completion percentage
- Better role-based login redirects
- Advanced form validation
- PostgreSQL database
- Production static file configuration
- Cloud media storage
- Environment variables
- HTTPS
- Production security configuration
- Production deployment

---

## Production

The current project is mainly a learning and portfolio project.

Before using it in production, the following should be configured:

- DEBUG = False
- Environment variables
- Production database such as PostgreSQL
- Static files
- Media storage
- HTTPS
- Secure cookies
- CSRF security
- ALLOWED_HOSTS
- Error logging
- Production server

---

## Portfolio Description

CareerHub is a Django-based Job and Internship Portal that connects students with companies.

The platform allows students to create professional profiles, upload resumes, search for jobs, apply for opportunities and track application status.

Companies can create profiles, post jobs and internships, manage their job postings, view applicants and update application status.

The project demonstrates practical knowledge of Django ORM, Models, ModelForms, Authentication, Authorization, CRUD operations, File Uploads, Search and Filtering, Database Relationships, Django Admin, Templates, Bootstrap and Git/GitHub.

---

## Learning Flow

Django Project Setup

↓

Models

↓

Migrations

↓

Django Admin

↓

Forms

↓

Views

↓

URLs

↓

Templates

↓

Authentication

↓

Authorization

↓

CRUD Operations

↓

File Uploads

↓

Search & Filtering

↓

Job Applications

↓

Dashboards

↓

Bootstrap UI

↓

Git & GitHub

---

## Author

CareerHub was developed as a practical Django project to learn and demonstrate backend development concepts using Python and Django.
