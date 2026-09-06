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


def get_valid_deadline(message):
    while True:
        date_input = input(message).strip()

        if is_valid_date(date_input):
            deadline_date = datetime.strptime(date_input, "%Y-%m-%d")

            if deadline_date.date() > datetime.today().date():
                return date_input
            else:
                print("The deadline must be a date in the future ")
        else:
            print("Please enter a valid date format ")


def is_valid_amount(amount):
    try:
        return float(amount) > 0
    except (ValueError, TypeError):
        return False


def get_valid_title(message):
    while True:
        title = input(message).strip()

        if not title:
            print("Title cannot be empty or just spaces, Try again.")
        elif len(title) < 3:
            print("Title must be at least 3 characters long.")
        elif len(title) > 50:
            print("Title cannot exceed 50 characters.")
        else:
            return title


def get_valid_amount(message):
    while True:
        amount = input(message).strip()
        try:
            valid_amount = float(amount)

            if valid_amount > 0:
                return valid_amount
            else:
                print("Amount must be greater than 0")

        except ValueError:
            print("Please enter a valid number")
