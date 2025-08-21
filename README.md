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
