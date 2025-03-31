# Reservation Management System

This project is a Django-based web application for managing reservations. It allows users to sign up, log in, and book reservations. Admins can view, add, and edit reservations through the Django admin interface.

---

## Features

### User Features:
1. **Sign Up**: Users can create an account to access the system.
2. **Log In**: Users can log in to their accounts.
3. **Book a Reservation**: Authenticated users can book a reservation by filling out a form.
4. **View Reservations**: Users can view their own reservations.
5. **Log Out**: Users can log out of their accounts.

### Admin Features:
1. **View All Reservations**: Admins can view a list of all reservations.

---

## Pages and Flow

1. **Sign Up Page** (`/signup`):
   - The default page when the application starts.
   - Allows users to create an account.

2. **Log In Page** (`/login`):
   - After signing up, users are redirected here to log in.

3. **Main Page** (`/index`):
   - The main page users see after logging in.
   - Displays a logout button.

4. **Booking Page** (`/booking`):
   - Allows users to book a reservation.

5. **User Reservations Page** (`/user-bookings/`):
   - Displays a list of reservations made by the logged-in user.

6. **Admin Page** (`/admin/`):
   - Accessible only to superusers.
   - Allows admins to view, add, edit, and delete reservations.

---
## Dependencies

The project uses the following dependencies:
- **Python 3.12+**
- **Django 5.1.7**
- **Poetry**: For dependency management.
- **Docker** and **Docker Compose**: For containerized deployment.

## How to Run 

    poetry install
    make compose.start
    make migrate
    make createsuperuser


### Prerequisites:
- Docker and Docker Compose installed.
- Poetry installed for dependency management.

### Setup:
   Clone the repository:
   git clone <https://github.com/DiogoLpes/backend-i.git>
   cd <project>


