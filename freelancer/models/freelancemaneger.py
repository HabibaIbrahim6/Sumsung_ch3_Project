import json
from .user import Client, Freelancer
from .project import Project
from .invoice import Invoice


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

        choice = int(input("Enter your choice (1-3): "))

        while choice not in range(1, 4):
            print("Invalid choice. Please try again.")
            choice = int(input("Enter your choice (1-3): "))

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
        else:
            user = self.users[user_id]

        if user.check_password(password):
            print("Login success")
        else:
            print("Wrong password.")

    def register_client(self, name, phone_num, password):

        user_id = f"C{len(self.users) + 1}"

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

        user_id = f"F{len(self.users) + 1}"

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