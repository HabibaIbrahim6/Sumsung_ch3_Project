import json
from client import Client
from .freelancer import Freelancer
from .project import Project
from .invoice import Invoice
from ..utils import helper_functions
from ..utils import validators
from ..menus.freelancer_menu import FreelancerMenu
from ..menus.client_menu import ClientMenu

class FreelanceManager:
    def __init__(self):
        self.users = {}
        self.load_users()

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

    def save_users(self):
        with open("data.jsonl", "w") as file:
            for user in self.users.values():
                file.write(json.dumps(user.to_dict()) + "\n")

    def login(self, user_id, password):
        
        if user_id not in self.users:
            print("User not found.")
            return

        user = self.users[user_id]

        if validators.check_password(user,password):
            print("Login success")
        else:
            print("Wrong password.")
            return

        if isinstance(user, Client):
            client_menu = ClientMenu(user, self)
            client_menu.show_menu()

        elif isinstance(user, Freelancer):
            freelancer_menu = FreelancerMenu(user, self)
            freelancer_menu.show_menu()

    def register_client(self, name, phone_num, password):

        user_id = helper_functions.generate_id("C", len(self.users) + 1)

        client = Client(
            user_id,
            name,
            phone_num,
            password
        )

        self.users[user_id] = client

        self.save_users()

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

        self.save_users()

        print("registered successfully.")

