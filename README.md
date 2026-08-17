# 🏟️ BookMyTurf

### Django-based Turf Booking & Management Platform

BookMyTurf is a full-stack web application designed to simplify the process of discovering, booking, and managing sports turf facilities online.

The platform provides separate workflows for **customers, turf owners, and administrators**, allowing users to search for available turfs, reserve time slots, make online payments, and manage their bookings.

---
## ✨ Features

### 👤 User Features

- 🔐 User registration and login
- 🔎 Search and browse available turfs
- 📍 View turf information and availability
- 📅 Select preferred date and time slots
- 💳 Online payment integration for bookings
- ❌ Cancel bookings within the allowed cancellation period
- 👤 View and update profile information
- 📋 View current and previous bookings
- 📊 Access booking history

### 🏟️ Turf Owner Features

- 📝 Register a turf facility
- ⏳ Submit turf registration for admin approval
- 🏟️ Manage turf information
- 📅 Manage turf availability and bookings
- 📋 Monitor bookings for registered turfs
- 📊 Access a dedicated turf-owner dashboard

### 🛠️ Administrator Features

- 👥 Manage registered users
- 🏟️ Review and approve turf registrations
- 📋 Monitor and manage bookings
- 🏟️ Manage available turf listings
- 📊 Access a dedicated administrator dashboard

### 🔐 Role-Based Access Control

The system provides separate access and dashboards for:

- **Users**
- **Turf Owners**
- **Administrators**

Each role has access to the features and operations relevant to their responsibilities.

---

## 🛠️ Technologies Used

### Backend
- **Python**
- **Django**

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript**

### Database
- **SQLite3**

### Other
- Django ORM
- Django Authentication
- Role-Based Access Control
- Online Payment Integration
---

## 🔄 Application Workflow

The BookMyTurf platform follows a role-based workflow:

### 👤 User Booking Flow

```text
User Registration / Login
          ↓
     Browse Turfs
          ↓
   View Turf Details
          ↓
 Select Date & Time Slot
          ↓
   Make Online Payment
          ↓
    Booking Confirmed
          ↓
    View Booking History


🏟️ Turf Owner Flow
Turf Owner Registration
          ↓
   Submit Turf Details
          ↓
   Admin Review & Approval
          ↓
    Turf Becomes Available
          ↓
   Manage Turf & Bookings

🛠️ Administrator Flow
Administrator Login
        ↓
Manage Users
        ↓
Review Turf Registrations
        ↓
Approve / Manage Turfs
        ↓
Monitor Bookings
