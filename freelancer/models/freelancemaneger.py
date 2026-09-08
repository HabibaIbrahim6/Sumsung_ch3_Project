import json
from .client import Client
from .freelancer import Freelancer
from .project import Project

from ..utils import helper_functions

from ..menus.freelancer_menu import FreelancerMenu
from ..menus.client_menu import ClientMenu


class FreelanceManager:

    def __init__(self):
        self.users = {}
        self.projects = []
        self.load_users()

    def load_users(self):
        try:
            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)

        except FileNotFoundError:
            print("data.json not found")
            return

        except json.JSONDecodeError:
            print("data.json is corrupted or invalid")
            return

        for user_data in data:

            if "user_id" not in user_data:
                print("User ID not found, skipping...")
                continue

            user_id = str(user_data["user_id"])
            role = user_data.get("role")

            if role == "Client":
                user = Client.from_dict(user_id, user_data)

            elif role == "Freelancer":
                user = Freelancer.from_dict(user_id, user_data)

            else:
                print(f"Unknown role for user {user_id}, skipping...")
                continue

            self.users[user_id] = user

        self.rebuild_relationships()
    def rebuild_relationships(self):

        self.projects = []
        for user in self.users.values():
            if isinstance(user, Client):
                for project in user.projects_created:
                    if project not in self.projects:
                        self.projects.append(project)

        for user in self.users.values():
            if not isinstance(user, Freelancer):
                continue

            project_ids = getattr(user,"_assigned_project_ids",[])
            user.assigned_projects = []

            for project_id in project_ids:
                project = self.get_project_by_id(project_id)

                if project is None:
                    continue

                if project not in user.assigned_projects:
                    user.assigned_projects.append(project)

                project.freelancer = user

        for user in self.users.values():

            if not isinstance(user, Freelancer):
                continue

            requests = getattr(user,"_received_request_data",[])

            user.received_requests = []

            for request_data in requests:

                project_id = request_data.get("project_id")
                client_id = request_data.get("client_id")

                project = self.get_project_by_id(project_id)
                client = self.users.get(str(client_id))

                if project is None or client is None:
                    continue

                request = {
                    "project": project,
                    "client": client,
                    "message": request_data.get("message", ""),
                    "status": request_data.get("status", "pending")
                }

                user.received_requests.append(request)

    def get_project_by_id(self, project_id):

        if project_id is None:
            return None

        project_id = str(project_id)

        for project in self.projects:

            if str(project.id) == project_id:
                return project

        return None

    def save_users(self):

        data = []

        try:
            for user in self.users.values():
                user_data = user.to_dict()
                json.dumps(user_data) 
                data.append(user_data)

        except Exception as error:
            print("\nERROR: Could not save data.")
            print(f"Reason: {error}")
            print("The existing data.json file was NOT changed.")
            return False

        try:
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            return True

        except Exception as error:
            print("\nERROR: Could not write data.json.")
            print(f"Reason: {error}")
            return False
            

    def login(self, user_id, password):

        user_id = str(user_id).strip()

        if user_id not in self.users:
            print("User not found.")
            return None

        user = self.users[user_id]

        if password != user.password:
            print("Wrong password.")
            return None

        print("\nLogin success.")

        if isinstance(user, Client):

            client_menu = ClientMenu(user,self)
            client_menu.show_menu()

        elif isinstance(user, Freelancer):

            freelancer_menu = FreelancerMenu(user,self)
            freelancer_menu.show_menu()

        

    def register_client(self,name,email,password):

        user_id = helper_functions.generate_id("C",len(self.users) + 1)

        client = Client(user_id,name,email,password)

        self.users[user_id] = client

        if not self.save_users():
            del self.users[user_id]
            print("Registration failed because ","the data could not be saved.")

            return None

        print("\nRegistered successfully.")
        print(f"Your ID is: {user_id}")
        return client

    def register_freelancer(self,name,email,password,skills):

        user_id = helper_functions.generate_id("F",len(self.users) + 1)

        freelancer = Freelancer(user_id,name,email,password,skills)

        self.users[user_id] = freelancer

        if not self.save_users():

            del self.users[user_id]

            print("Registration failed because ","the data could not be saved ")

            return None

        print("\nRegistered successfully.")
        print(f"Your User ID is: {user_id}")

        return freelancer

    def add_project(self, project):

        if not isinstance(project, Project):
            raise TypeError("project must be a Project object.")

        if project not in self.projects:
            self.projects.append(project)

    def get_freelancers(self):

        freelancers = []

        for user in self.users.values():

            if isinstance(user, Freelancer):
                freelancers.append(user)

        return freelancers

    def get_clients(self):

        clients = []

        for user in self.users.values():

            if isinstance(user, Client):
                clients.append(user)

        return clients