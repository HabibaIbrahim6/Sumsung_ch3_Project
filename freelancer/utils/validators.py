import re
from datetime import datetime


# ---------- Regex Patterns ----------

EMAIL_PATTERN = re.compile(r"^[\w.]+@(gmail|yahoo)\.com$")
PASSWORD_PATTERN = re.compile(r"^(?=.*\d)(?=.*[!@#$%^&*]).{9,}$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# ---------- Validation Functions ----------

def is_valid_email(email):
    return bool(EMAIL_PATTERN.fullmatch(email))


def is_valid_password(password):
    return bool(PASSWORD_PATTERN.fullmatch(password))


def is_valid_date(date):
    if not DATE_PATTERN.fullmatch(date):
        return False

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_amount(amount):
    try:
        return float(amount) > 0
    except (ValueError, TypeError):
        return False