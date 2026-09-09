import re 
from datetime import datetime

#  Regex Patterns 

EMAIL_PATTERN = re.compile(r"^[\w.]+@(gmail|yahoo)\.com$")
PASSWORD_PATTERN = re.compile(r"^(?=.*\d)(?=.*[!@#$%^&*]).{9,}$")
PHONE_PATTERN = re.compile(r"01[0125]\d{8}")


#  Validation Functions 

def is_valid_email(email):
    return bool(EMAIL_PATTERN.fullmatch(email))


def is_valid_password(password):
    return bool(PASSWORD_PATTERN.fullmatch(password))

def check_password(self, password):
        return self.password == password


def get_valid_deadline(message):

    while True:

        date_input = input(message).strip()

        try:
            deadline_date = datetime.strptime(
                date_input,
                "%d/%m/%Y"
            )

            if deadline_date.date() < datetime.today().date():
                print("Invalid date. Deadline cannot be in the past.")
                continue

            return deadline_date.strftime("%Y-%m-%d")

        except ValueError:
            print(
                "Invalid date. Please enter a valid date as DD/MM/YYYY."
            )

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
