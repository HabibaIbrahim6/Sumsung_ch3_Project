from .user import User
from .project import Project


class Freelancer(User):

    def __init__(self, user_id, name, email, password, skills):

        super().__init__(
            user_id,
            name,
            email,
            password,
            "Freelancer"
        )

        self.skills = skills
        self.received_requests = []
        self.assigned_projects = []
        self._assigned_project_ids = []
        self._received_request_data = []

    def display_profile(self):

        super().display_profile()

        print(f"Skills: {', '.join(self.skills)}")
        print(f"Assigned Projects: {len(self.assigned_projects)}")

        if not self.assigned_projects:
            print("No assigned projects yet.")
        else:
            print("\nAssigned projects:")

            for project in self.assigned_projects:
                print(project)

    def assign_project(self, project):

        if not isinstance(project, Project):
            raise TypeError("project must be a Project object.")

        if project in self.assigned_projects:
            print("Project is already assigned.")
            return False

        self.assigned_projects.append(project)
        project.assign_freelancer(self)

        return True

    def get_project_by_id(self, project_id):

        project_id = str(project_id)

        for project in self.assigned_projects:

            if str(project.id) == project_id:
                return project

        return None

    def add_request(self, request):

        if request in self.received_requests:
            raise ValueError("This request already exists.")

        self.received_requests.append(request)

        print("Project request added successfully.")

    def get_pending_requests(self):

        return [
            request
            for request in self.received_requests
            if request.get("status") == "pending"
        ]

    def get_completed_projects(self):

        return [
            project
            for project in self.assigned_projects
            if project.status == "Completed"
        ]

    def to_dict(self):

        data = super().to_dict()

        data["skills"] = self.skills

        data["assigned_projects"] = [
            project.id
            for project in self.assigned_projects
        ]

        data["received_requests"] = []

        for request in self.received_requests:

            project = request.get("project")
            client = request.get("client")

            data["received_requests"].append({
                "project_id": project.id if project else None,
                "client_id": client.id if client else None,
                "message": request.get("message", ""),
                "status": request.get("status", "pending")
            })

        return data

    @classmethod
    def from_dict(cls, user_id, user_data):

        freelancer = cls(
            user_id,
            user_data["name"],
            user_data["email"],
            user_data["password"],
            user_data.get("skills", [])
        )

        freelancer.assigned_projects = []
        freelancer.received_requests = []

        freelancer._assigned_project_ids = user_data.get(
            "assigned_projects",
            []
        )

        freelancer._received_request_data = user_data.get(
            "received_requests",
            []
        )

        return freelancer