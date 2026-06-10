# 📚 API Documentation | توثيق الـ API

Complete REST API documentation for Dental Clinic Management System.

**Base URL:** `http://127.0.0.1:8000/api/`  
**Interactive Docs:** `http://127.0.0.1:8000/api/docs/` (Swagger UI)

---

## 📋 Table of Contents
- [Authentication](#authentication)
- [Appointments API](#appointments-api)
- [Patients API](#patients-api)
- [Doctors API](#doctors-api)
- [Error Handling](#error-handling)
- [Rate Limiting](#rate-limiting)

---

## 🔐 Authentication

The API uses Django Session Authentication by default. All protected endpoints require an active session (login via web interface).

### Login
```http
POST /login/
Content-Type: application/x-www-form-urlencoded

username=admin&password=admin123
```

### Check Authentication Status
```http
GET /api/schema/
```

**Response (Authenticated):** `200 OK`  
**Response (Unauthenticated):** `403 Forbidden`

---

## 📅 Appointments API

Base URL: `/api/appointments/`

### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/appointments/` | List all appointments |
| POST | `/api/appointments/` | Create new appointment |
| GET | `/api/appointments/{id}/` | Get appointment details |
| PUT | `/api/appointments/{id}/` | Update appointment |
| PATCH | `/api/appointments/{id}/` | Partial update |
| DELETE | `/api/appointments/{id}/` | Delete appointment |

### 1. List Appointments

```http
GET /api/appointments/?search=ahmed&status=PENDING
```

**Query Parameters:**
- `search` (optional): Search by patient name
- `status` (optional): Filter by status (PENDING, CONFIRMED, COMPLETED, CANCELLED)
- `page` (optional): Page number for pagination
- `page_size` (optional): Items per page (default: 20, max: 100)

**Example Response:**
```json
[
  {
    "id": 1,
    "patient": 1,
    "doctor": 1,
    "patient_detail": {
      "id": 1,
      "user": {
        "id": 3,
        "username": "patient1",
        "email": "patient1@email.com",
        "role": "PATIENT",
        "phone_number": null
      },
      "full_name": "Ahmed Ali",
      "email": "patient1@email.com",
      "age": 30,
      "phone_number": "07701234567",
      "medical_history": "No history"
    },
    "doctor_detail": {
      "id": 1,
      "user": {
        "id": 2,
        "username": "doctor1",
        "email": "doctor1@dental.com",
        "role": "DOCTOR",
        "phone_number": null
      },
      "full_name": "د. Doctor One",
      "specialization": "طبيب أسنان عام",
      "bio": "Expert dentist",
      "working_hours": "9 ص - 5 م",
      "is_active": true,
      "total_appointments": 5,
      "today_appointments": 2
    },
    "date": "2026-06-15",
    "time": "10:00:00",
    "status": "PENDING",
    "status_display": "قيد الانتظار",
    "notes": "فحص دوري"
  }
]
```

### 2. Create Appointment

```http
POST /api/appointments/
Content-Type: application/json

{
  "patient": 1,
  "doctor": 1,
  "date": "2026-06-20",
  "time": "14:30:00",
  "status": "PENDING",
  "notes": "صيانة دورية"
}
```

**Required Fields:**
- `patient` (integer): Patient ID
- `doctor` (integer): Doctor ID
- `date` (string): Date in YYYY-MM-DD format
- `time` (string): Time in HH:MM:SS format

**Optional Fields:**
- `status` (string): PENDING, CONFIRMED, COMPLETED, CANCELLED (default: PENDING)
- `notes` (string): Additional notes

**Success Response:** `201 Created`
```json
{
  "id": 2,
  "patient": 1,
  "doctor": 1,
  "patient_detail": { ... },
  "doctor_detail": { ... },
  "date": "2026-06-20",
  "time": "14:30:00",
  "status": "PENDING",
  "status_display": "قيد الانتظار",
  "notes": "صيانة دورية"
}
```

**Error Response:** `400 Bad Request`
```json
{
  "error": "هذا الطبيب لديه موعد آخر في نفس الوقت المحدد."
}
```

### 3. Get Appointment Details

```http
GET /api/appointments/1/
```

**Success Response:** `200 OK`
```json
{
  "id": 1,
  "patient": 1,
  "doctor": 1,
  "patient_detail": { ... },
  "doctor_detail": { ... },
  "date": "2026-06-15",
  "time": "10:00:00",
  "status": "PENDING",
  "status_display": "قيد الانتظار",
  "notes": "فحص دوري"
}
```

**Error Response:** `404 Not Found`
```json
{
  "detail": "Not found."
}
```

### 4. Update Appointment

```http
PUT /api/appointments/1/
Content-Type: application/json

{
  "patient": 1,
  "doctor": 1,
  "date": "2026-06-16",
  "time": "11:00:00",
  "status": "CONFIRMED",
  "notes": "تم تأكيد الموعد"
}
```

**Success Response:** `200 OK`

### 5. Partial Update (Patch)

```http
PATCH /api/appointments/1/
Content-Type: application/json

{
  "status": "COMPLETED",
  "notes": "تمت الزيارة بنجاح"
}
```

**Success Response:** `200 OK`

### 6. Delete Appointment

```http
DELETE /api/appointments/1/
```

**Success Response:** `200 OK`
```json
{
  "message": "تم حذف الموعد"
}
```

---

## 👤 Patients API

Base URL: `/api/patients/`

### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/patients/` | List all patients |
| POST | `/api/patients/` | Create new patient |
| GET | `/api/patients/{id}/` | Get patient details |
| PUT | `/api/patients/{id}/` | Update patient |
| PATCH | `/api/patients/{id}/` | Partial update |
| DELETE | `/api/patients/{id}/` | Delete patient |

### 1. List Patients

```http
GET /api/patients/
```

**Example Response:**
```json
[
  {
    "id": 1,
    "user": {
      "id": 3,
      "username": "patient1",
      "email": "patient1@email.com",
      "role": "PATIENT",
      "phone_number": null
    },
    "full_name": "Ahmed Ali",
    "email": "patient1@email.com",
    "age": 30,
    "phone_number": "07701234567",
    "medical_history": "No history",
    "created_at": "2026-06-11T10:30:00Z"
  }
]
```

### 2. Create Patient

```http
POST /api/patients/
Content-Type: application/json

{
  "username": "newpatient",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@email.com",
  "password": "securepass123",
  "age": 25,
  "phone_number": "07709876543",
  "medical_history": "No allergies"
}
```

**Success Response:** `201 Created`
```json
{
  "id": 2,
  "user": {
    "id": 5,
    "username": "newpatient",
    "email": "john@email.com",
    "role": "PATIENT",
    "phone_number": null
  },
  "full_name": "John Doe",
  "email": "john@email.com",
  "age": 25,
  "phone_number": "07709876543",
  "medical_history": "No allergies",
  "created_at": "2026-06-11T12:00:00Z"
}
```

**Validation Errors:** `400 Bad Request`
```json
{
  "username": ["اسم المستخدم موجود مسبقاً"],
  "age": ["العمر يجب أن يكون بين 0 و 150 سنة"],
  "phone_number": ["Invalid Iraqi phone number format. Use: 07x xxx xxxx"]
}
```

### 3. Get Patient Details

```http
GET /api/patients/1/
```

### 4. Update Patient

```http
PATCH /api/patients/1/
Content-Type: application/json

{
  "age": 31,
  "medical_history": "Updated medical history"
}
```

---

## 👨‍⚕️ Doctors API

Base URL: `/api/doctors/`

### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/doctors/` | List all doctors |
| POST | `/api/doctors/` | Create new doctor |
| GET | `/api/doctors/{id}/` | Get doctor details |
| PUT | `/api/doctors/{id}/` | Update doctor |
| PATCH | `/api/doctors/{id}/` | Partial update |
| DELETE | `/api/doctors/{id}/` | Delete doctor |

### 1. List Doctors

```http
GET /api/doctors/
```

**Example Response:**
```json
[
  {
    "id": 1,
    "user": {
      "id": 2,
      "username": "doctor1",
      "email": "doctor1@dental.com",
      "role": "DOCTOR",
      "phone_number": null
    },
    "full_name": "د. Doctor One",
    "specialization": "طبيب أسنان عام",
    "bio": "Expert dentist with 10 years experience",
    "working_hours": "9 ص - 5 م",
    "is_active": true,
    "total_appointments": 15,
    "today_appointments": 3,
    "created_at": "2026-06-11T08:00:00Z"
  }
]
```

### 2. Get Doctor Details

```http
GET /api/doctors/1/
```

### 3. Create Doctor

```http
POST /api/doctors/
Content-Type: application/json

{
  "username": "newdoctor",
  "first_name": "Dr. Sarah",
  "last_name": "Smith",
  "email": "sarah@dental.com",
  "password": "doctor123",
  "specialization": "جراحة فم وفكين",
  "bio": "Expert in oral surgery",
  "working_hours": "10 ص - 6 م"
}
```

---

## Status Codes Reference

| Status Code | Meaning | Arabic |
|-------------|---------|--------|
| 200 | OK | نجاح |
| 201 | Created | تم الإنشاء |
| 400 | Bad Request | طلب غير صالح |
| 401 | Unauthorized | غير مصرح |
| 403 | Forbidden | مرفوض |
| 404 | Not Found | غير موجود |
| 500 | Server Error | خطأ في الخادم |

---

## Data Models

### Appointment Status
```
PENDING    - قيد الانتظار
CONFIRMED  - تم التأكيد
COMPLETED  - تمت الزيارة
CANCELLED  - ملغي
```

### User Roles
```
ADMIN        - مدير النظام
DOCTOR       - طبيب
RECEPTIONIST - موظف استقبال
PATIENT      - مريض
```

---

## Example Usage with JavaScript

```javascript
// Fetch appointments
async function getAppointments() {
  const response = await fetch('/api/appointments/', {
    method: 'GET',
    headers: {
      'Accept': 'application/json',
    },
    credentials: 'include'  // Include session cookie
  });
  
  const data = await response.json();
  return data;
}

// Create appointment
async function createAppointment(patientId, doctorId, date, time) {
  const response = await fetch('/api/appointments/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    credentials: 'include',
    body: JSON.stringify({
      patient: patientId,
      doctor: doctorId,
      date: date,
      time: time,
      status: 'PENDING',
      notes: 'New appointment'
    })
  });
  
  return await response.json();
}

// Delete appointment
async function deleteAppointment(id) {
  const response = await fetch(`/api/appointments/${id}/`, {
    method: 'DELETE',
    credentials: 'include'
  });
  
  return await response.json();
}
```

---

## Example Usage with Python

```python
import requests

# Login first
session = requests.Session()
session.post('http://127.0.0.1:8000/login/', {
    'username': 'admin',
    'password': 'admin123'
})

# Get appointments
response = session.get('http://127.0.0.1:8000/api/appointments/')
appointments = response.json()

# Create appointment
new_appointment = {
    'patient': 1,
    'doctor': 1,
    'date': '2026-06-20',
    'time': '10:00:00',
    'status': 'PENDING',
    'notes': 'Regular checkup'
}

response = session.post(
    'http://127.0.0.1:8000/api/appointments/',
    json=new_appointment
)
print(response.json())
```

---

## Error Handling

### Standard Error Format
```json
{
  "detail": "Error message",
  "code": "error_code"
}
```

### Validation Errors
```json
{
  "field_name": [
    "Error message for this field"
  ]
}
```

---

**📖 For interactive documentation, visit:** http://127.0.0.1:8000/api/docs/
