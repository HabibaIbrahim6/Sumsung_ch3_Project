from .user import User
from .project import Project

class Client(User):

    def __init__(self, user_id, name, email, password):
        super().__init__(user_id,name,email,password,"Client")

        self.projects_created = []
        self.sent_requests = []
        self.messages = []

   
    def add_project(self, project):
        if not isinstance(project, Project):
            raise TypeError("project must be a Project object.")

        if project in self.projects_created:
            raise ValueError("This project already exists.")

        self.projects_created.append(project)

        print("Project created successfully.")

        return project
    
    def view_projects(self):
        
        if not self.projects_created:
            print("No projects created yet.")
            return

        print("========== MY PROJECTS ==========")

        for project in self.projects_created:
            print(project)

    def get_project_by_id(self, project_id) -> "Project | None":

        for project in self.projects_created:

            if project.id == project_id:
                return project

        return None

    def delete_project(self, project_id):
        project = self.get_project_by_id(project_id)

        if project is None:
            print("Project not found.")
            return False

        self.projects_created.remove(project)
        return True

    
    def add_request(self, request):

        if request in self.sent_requests:
            raise ValueError("This request already exists.")

        self.sent_requests.append(request)

        print("Project request added to client history")

        return request
    
    def get_requests(self):
        return self.sent_requests

    def get_request_by_id(self, request_id):

        for request in self.sent_requests:

            if request.id == request_id:
                return request

        return None

    def view_requests(self):
        if not self.sent_requests:
            print("No project requests sent yet.")
            return

        print("\n========== SENT REQUESTS ==========")

        for request in self.sent_requests:
            project = request.get("project")
            freelancer_id = request.get("freelancer_id")
            message = request.get("message", "")
            status = request.get("status", "pending")

            print(f"Project ID: {project.id}")
            print(f"Project Title: {project.title}")
            print(f"Freelancer ID: {freelancer_id}")
            print(f"Message: {message}")
            print(f"Status: {status}")
            print("-" * 40)

    def add_message(self, message):
        self.messages.append(message)

        print("Message received successfully.")

        return message
    
    def get_messages(self):
        return self.messages

    def view_messages(self):

        if not self.messages:
            print("No messages yet.")
            return

        print("========== MESSAGES ==========")

        for message in self.messages:
            print(message)

    def display_profile(self):
        super().display_profile() 

        print(f"Projects Created: {len(self.projects_created)}")

        print(f"Sent Requests: {len(self.sent_requests)}")

        print(f"Messages: {len(self.messages)}")

    
    def to_dict(self):
        return {
            "user_id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "role": self.role,

            "projects_created": [project.to_dict()for project in self.projects_created],

            "sent_requests": [],

            "messages": []
        }

    @classmethod
    def from_dict(cls, user_id, data):
        client = cls(
            user_id,
            data["name"],
            data["email"],
            data["password"]
        )

        for project_data in data.get("projects_created",[]):

            project = Project.from_dict(project_data,client)

            client.projects_created.append(project)

        return client
