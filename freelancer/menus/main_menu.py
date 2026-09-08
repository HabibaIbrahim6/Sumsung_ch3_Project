from typing import TYPE_CHECKING

from ..utils import validators as val
from ..utils import helper_functions

if TYPE_CHECKING:
    from ..models.freelancemaneger import FreelanceManager


class MainMenu:

    def __init__(self, manager: "FreelanceManager"):
        self.manager = manager

    def show_menu(self):

        while True:

            print("\n========================================")
            print("       SIC FREELANCE PROJECT HUB")
            print("========================================")
            print("1. Login")
            print("2. Register as Client")
            print("3. Register as Freelancer")
            print("4. Quit")
            print("========================================")

            choice = helper_functions.get_menu_choice(1, 4)

            if choice == 1:
                self.login_page()

            elif choice == 2:
                self.register_client_page()

            elif choice == 3:
                self.register_freelancer_page()

            elif choice == 4:
                print("Thank you for using SIC Freelance Project Hub!")
                break

   
    def login_page(self):

        print("\n========== LOGIN ==========")

        while True:

            user_id = input("Enter your user ID: ").strip()
            password = input("Enter your password: ").strip()

            if not user_id or not password:
                print("User ID and password cannot be empty.")
                continue

            break

        user = self.manager.login(user_id, password)

        if not user:
            print("Login failed. Please check your credentials.")
            return

    
    def register_client_page(self):

        print("====== REGISTER AS CLIENT ======")

        while True:
            name = input("Enter your name: ").strip()
            if name:
                break
            print("Name cannot be empty.")

        while True:
            email = input("Enter your email: ").strip()

            if val.is_valid_email(email):
                break

            print("Invalid email format.")


        while True:

            password = input(
                "Enter your password: "
            ).strip()

            if val.is_valid_password(password):
                break

            print("Invalid password",
                  "Password must:",
                  "- contain at least 9 characters",
                  "- contain at least one digit",
                  "- contain at least one special character",)

        self.manager.register_client(name,email,password)

    def register_freelancer_page(self):

        print("\n====== REGISTER AS FREELANCER ======")
        while True:

            name = input("Enter your name: ").strip()

            if name:
                break

            print("Name cannot be empty.")

        while True:

            email = input("Enter your email: ").strip()

            if val.is_valid_email(email):
                break

            print("Invalid email format.")

        while True:

            password = input("Enter your password: ").strip()

            if val.is_valid_password(password):
                break

            print("Invalid password",
                "Password must:",
                "- contain at least 9 characters",
                "- contain at least one digit",
                "- contain at least one special character",)
            


        while True:

            skills_input = input("Enter your skills separated by comma (,): ").strip()

            skills = [skill.strip()for skill in skills_input.split(",")if skill.strip()]

            if skills:
                break

            print("Please enter at least one skill.")

     
        self.manager.register_freelancer( name,email,password,skills)