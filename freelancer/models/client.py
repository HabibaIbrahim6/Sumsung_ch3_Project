from .user import User
from .project import Project


class Client(User):

    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password, "Client")

        # projects_created will hold the projects that the client has created
        self.projects_created = []

        # sent_requests will hold the project requests
        # that the client has sent to freelancers
        self.sent_requests = []

        # messages will hold the messages that the client has received
        self.messages = []


    def create_project(self, project):
        """
        Add a new project to the client's projects.
        """

        # Make sure the object is a Project
        if not isinstance(project, Project):
            raise TypeError("project must be a Project object.")

        # Prevent adding the same project twice
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

        print("\n===== My Projects =====")

        for project in self.projects_created:
            print(project)

    def get_project_by_id(self, project_id):
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

    # Request Methods
    def add_request(self, request):
        """
        Add a project request sent by the client.
        """

        if request in self.sent_requests:
            raise ValueError("This request already exists.")

        self.sent_requests.append(request)

        print("Project request sent successfully.")

        return request

    def get_requests(self):
        """
        Return all project requests sent by the client.
        """

        return self.sent_requests

    def get_request_by_id(self, request_id):
        """
        Find a project request using its ID.
        """

        for request in self.sent_requests:

            if request.id == request_id:
                return request

        return None

    def view_requests(self):
        """
        Display all project requests sent by the client.
        """

        if not self.sent_requests:
            print("No project requests sent yet.")
            return

        print("\n===== Sent Project Requests =====")

        for request in self.sent_requests:
            print(request)

    
    # message Methods
    def add_message(self, message):
        """
        Add a received message to the client's messages.
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

        print("\n===== Messages =====")

        for message in self.messages:
            print(message)

    # profile Methods
    def display_profile(self):
        """
        Display the client's profile information.
        """

        # Call the parent User display_profile method
        super().display_profile()

        print(f"Projects Created: {len(self.projects_created)}")
        print(f"Sent Requests: {len(self.sent_requests)}")
        print(f"Messages: {len(self.messages)}")