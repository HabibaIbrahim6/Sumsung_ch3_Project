from user import User
from project import Project


class Client(User):

    def __init__(self, user_id, name, email, password):
        super().__init__(
            user_id,
            name,
            email,
            password,
            "Client"
        )

        # Projects created by this client
        self.projects_created = []

        # Project requests sent to freelancers
        self.sent_requests = []

        # Messages received from freelancers
        self.messages = []

   

    def add_project(self, project):
        """
        Add a new project to the client's projects.
        """

        if not isinstance(project, Project):
            raise TypeError("project must be a Project object.")

        if project in self.projects_created:
            raise ValueError("This project already exists.")

        self.projects_created.append(project)

        print("Project created successfully.")

        return project

    def view_projects(self):
        """
        Display all projects created by the client.
        """

        if not self.projects_created:
            print("No projects created yet.")
            return

        print("\n========== MY PROJECTS ==========")

        for project in self.projects_created:
            print(project)

    def get_project_by_id(self, project_id) -> "Project | None":
        """
        Find a project using its ID.
        """

        for project in self.projects_created:

            if project.id == project_id:
                return project

        return None

    def delete_project(self, project_id):
        """
        Delete a project using its ID.
        """

        project = self.get_project_by_id(project_id)

        if project is None:
            print("Project not found.")
            return False

        self.projects_created.remove(project)

        print("Project deleted successfully.")

        return True

    
    def add_request(self, request):

        if request in self.sent_requests:
            raise ValueError("This request already exists.")

        self.sent_requests.append(request)

        print("Project request added successfully.")

        return request

    def get_requests(self):
        """
        Return all project requests sent by the client.
        """

        return self.sent_requests

    def get_request_by_id(self, request_id):
        """
        Find a request using its ID.
        """

        for request in self.sent_requests:

            if request.id == request_id:
                return request

        return None

    def view_requests(self):
        """
        Display all requests sent by the client.
        """

        if not self.sent_requests:
            print("No project requests sent yet.")
            return

        print("\n========== SENT REQUESTS ==========")

        for request in self.sent_requests:
            print(request)

   
    def add_message(self, message):
        """
        Add a message received by the client.
        """

        self.messages.append(message)

        print("Message received successfully.")

        return message

    def get_messages(self):
        """
        Return all messages received by the client.
        """

        return self.messages

    def view_messages(self):
        """
        Display all messages received by the client.
        """

        if not self.messages:
            print("No messages yet.")
            return

        print("\n========== MESSAGES ==========")

        for message in self.messages:
            print(message)

   
    def display_profile(self):
        """
        Display the client's profile information.
        """

        super().display_profile()

        print(
            f"Projects Created: "
            f"{len(self.projects_created)}"
        )

        print(
            f"Sent Requests: "
            f"{len(self.sent_requests)}"
        )

        print(
            f"Messages: "
            f"{len(self.messages)}"
        )

    def to_dict(self):
        """
        Convert the Client object into a dictionary
        so it can be saved in JSON.
        """

        return {
            "user_id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "role": self.role,

            "projects_created": [
                project.to_dict()
                for project in self.projects_created
            ],

            "sent_requests": [],

            "messages": []
        }

    @classmethod
    def from_dict(cls, user_id, data):
        """
        Recreate a Client object from dictionary data.
        """

        client = cls(
            user_id,
            data["name"],
            data["email"],
            data["password"]
        )

        # Restore client's projects
        for project_data in data.get(
            "projects_created",
            []
        ):

            project = Project.from_dict(
                project_data,
                client
            )

            client.projects_created.append(project)

        return client
