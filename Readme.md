Django Project

Simple Django project built for learning and experimentation.
The project uses Django as the backend framework with a standard database setup and modular app structure.

---

Features

- Built with Django
- Clean project structure
- Easy to run locally
- Database migration ready
- Admin panel enabled

---

Tech Stack

- Python
- Django
- SQLite (default Django database)

---

Getting Started

Follow these steps to run the project locally.

1. Clone the repository

git clone https://github.com/username/repository-name.git
cd repository-name

2. Create virtual environment

python -m venv venv

Activate the environment:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run database migrations

python manage.py makemigrations
python manage.py migrate

5. Create admin user (optional)

python manage.py createsuperuser

6. Start the development server

python manage.py runserver

Open in browser:

http://127.0.0.1:8000

Admin panel:

http://127.0.0.1:8000/admin

---

Project Structure

project/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── apps/

---

Notes

- Make sure Python 3.9+ is installed.
- Do not commit sensitive files such as ".env" or local database files.
- Use virtual environments to keep dependencies isolated.

---

License

This project is open-source and available under the MIT License.