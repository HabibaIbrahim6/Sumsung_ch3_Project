import re # Regular expressions module for pattern matching
from datetime import datetime


# ---------- Regex Patterns ----------

EMAIL_PATTERN = re.compile(r"^[\w.]+@(gmail|yahoo)\.com$")
PASSWORD_PATTERN = re.compile(r"^(?=.*\d)(?=.*[!@#$%^&*]).{9,}$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


# ---------- Validation Functions ----------
# check if the email is valid
def is_valid_email(email):
    return bool(EMAIL_PATTERN.fullmatch(email))

# check if the password is valid
def is_valid_password(password):
    return bool(PASSWORD_PATTERN.fullmatch(password))

def is_valid_phone(phone):
    """
    Check if the phone number is a valid Egyptian mobile number.
    """
    return bool(re.fullmatch(r"01\d{9}", phone))

# check if the date is valid
def is_valid_date(date):
    if not DATE_PATTERN.fullmatch(date):
        return False
    # Check if the date is a valid calendar date
    try:
        # convert the string to a datetime object to validate the date
        # %Y: Year with century as a decimal number
        # %m: Month as a zero-padded decimal number
        # %d: Day of the month as a zero-padded decimal number
        datetime.strptime(date, "%Y-%m-%d")
        return True
    
    except ValueError:
        return False


def is_valid_amount(amount):
    try:
        return float(amount) > 0
    except (ValueError, TypeError):
        return False