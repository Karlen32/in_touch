

class Credentials:
    """Тестовые учётные данные (НЕ боевые)."""

    DOCTOR = {
        "email": "doctor@example.com",
        "password": "Password123!",
    }

    CLIENT = {
        "email": "client@example.com",
        "password": "Password123!",
    }

    ADMIN = {
        "email": "admin@example.com",
        "password": "Password123!",
    }

    INVALID_EMAIL = {
        "email": "invalid_email_format",
        "password": "Password123!",
    }

    INVALID_PASSWORD = {
        "email": DOCTOR["email"],
        "password": "short",
    }

    INVALID_CREDENTIALS = {
        "email": "unknown_user@example.com",
        "password": "WrongPass123!",
    }
