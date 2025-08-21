# Healthcare Backend API (Django + DRF + PostgreSQL)

## 🏥 Overview
Ye project ek **Healthcare Backend System** hai jisme users register/login karke **Patients**, **Doctors**, aur unke **Mappings** manage kar sakte hain.  
Backend Django REST Framework (DRF) aur PostgreSQL pe bana hai aur JWT authentication use karta hai.

---

## ⚙️ Features

1. **User Authentication**
   - User Registration (`/api/auth/register/`)
   - User Login (`/api/auth/login/`) with JWT token
   - Refresh JWT Token (`/api/auth/refresh/`)

2. **Patient Management**
   - Add Patient (Authenticated users only)
   - List Patients created by logged-in user
   - Retrieve/Update/Delete Patient

3. **Doctor Management**
   - Add Doctor
   - List all Doctors
   - Retrieve/Update/Delete Doctor

4. **Patient-Doctor Mapping**
   - Assign Doctor to Patient
   - List all Mappings
   - Get Doctors assigned to a Patient
   - Remove Mapping

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (`djangorestframework-simplejwt`)
- **Environment Config:** `.env` with `python-decouple`
- **Testing:** Postman / API Client

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd healthcare

2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure .env file

Create .env in root directory:

SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

5. Run migrations
python manage.py makemigrations
python manage.py migrate

6. Start server
python manage.py runserver


Server will run on: http://127.0.0.1:8000/
