import json
from .client import Client
from .freelancer import Freelancer
from .project import Project
from .invoice import Invoice
from ..utils import helper_functions
from ..utils import validators


class FreelanceManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def menu(self):
        print("Welcome to the Freelance Management System")
        print("1. Login")
        print("2. Register as Client")
        print("3. Register as Freelancer")
        print("---------------------------------")

        choice = helper_functions.get_menu_choice(1, 3)

        if choice == 1:
            user_id = input("Enter your user ID: ")
            password = input("Enter your password: ")
            self.login(user_id, password)

        elif choice == 2:
            name = input("Enter your name: ")
            phone_num = input("Enter your phone_num: ")
            password = input("Enter your password: ")

            self.register_client(name, phone_num, password)

        elif choice == 3:
            name = input("Enter your name: ")
            phone_num = input("Enter your phone_num: ")
            password = input("Enter your password: ")
            skills = input("Enter your skills with comma (,): ").split(",")

            self.register_freelancer(
                name,
                phone_num,
                password,
                skills
            )

    def load_users(self):
        try:
            with open("data.jsonl", "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    user_data = json.loads(line)
                    user_id = user_data["user_id"]

                    if user_data["role"] == "Client":
                        user = Client.from_dict(user_id, user_data)
                    elif user_data["role"] == "Freelancer":
                        user = Freelancer.from_dict(user_id, user_data)
                    else:
                        continue

                    self.users[user_id] = user

        except FileNotFoundError:
            return

    def append_user(self, user):
        with open("data.jsonl", "a") as file:
            file.write(json.dumps(user.to_dict()) + "\n")

    def login(self, user_id, password):

        if user_id not in self.users:
            print("User not found.")
            return

        user = self.users[user_id]

        if validators.check_password(password):
            print("Login success")
        else:
            print("Wrong password.")
            return

        if isinstance(user, Client):
            self.client_menu(user)

        if isinstance(user, Freelancer):
            self.freelancer_menu(user)
            pass

    def register_client(self, name, phone_num, password):

        user_id = helper_functions.generate_id("C", len(self.users) + 1)

        client = Client(
            user_id,
            name,
            phone_num,
            password
        )

        self.users[user_id] = client

        self.append_user(client)

        print("registered successfully")

    def register_freelancer(self, name, phone_num, password, skills):

        user_id = helper_functions.generate_id("F", len(self.users) + 1)

        freelancer = Freelancer(
            user_id,
            name,
            phone_num,
            password,
            skills
        )

        self.users[user_id] = freelancer

        self.append_user(freelancer)

        print("registered successfully.")

    def client_menu(self, current_client: Client):

        helper_functions.print_client_menu()

        choice = helper_functions.get_menu_choice(1, 5)

        if choice == 1: # create a project

            project_id = helper_functions.generate_id("P", len(current_client.projects_created) + 1)
            title = validators.get_valid_title("Enter project title: ")
            budget = validators.get_valid_amount("Enter the project budget: ")
            deadline = validators.get_valid_deadline("Enter the project deadline in YYYY-MM-DD format: ")
            milestones = helper_functions.get_milestones()
            new_project = Project(project_id, title, budget, current_client, deadline, milestones)
            current_client.add_project(new_project)

        elif choice == 2: # assign a project to a freelancer
            while True:
                project_id = input("Enter project ID: ")
                project = current_client.get_project_by_id(project_id)
                if project is None:
                    print("Project not found")
                elif project.status != "Open":
                    print("Project already assigned")
                else:
                    break
            while True:
                freelancer_id = input("Enter freelancer ID: ")
                freelancer = helper_functions.find_freelancer(self.users, freelancer_id)
                if freelancer is None:
                    print("Freelancer not found")
                else:
                    freelancer.assign_project(project)
                    project.assign_freelancer(freelancer)
                    print(f"Project '{project.title}' assigned to {freelancer.name}.")
                    break


        elif choice == 3:
            print("Enter the project ID:")
            project_id = input()
            current_project = current_client.get_project_by_id(project_id)

            if current_project is None:
                print("Project ID not found.")

            else:
                current_project.print_milestones()

                milestone_choice = helper_functions.get_menu_choice(1, len(current_project.milestones),
                                                                    "Choose milestone to update")

                current_milestone = current_project.milestones[milestone_choice - 1]
                new_status = helper_functions.get_new_milestone_status()
                current_milestone.update_status(new_status)
                current_project.update_project_status()


        elif choice == 4:
            pass
        elif choice == 5:
            # I want to return to log in/regester menu
            pass
