from .user import User
from .project import Project


class Freelancer(User):
    def __init__(self, user_id, name, phone_num, password, skills):
        super().__init__(user_id, name, phone_num, password, "Freelancer")
        self.skills = skills
        self.assigned_projects = []

    def display_profile(self):
        super().display_profile()

        if not self.assigned_projects:
            print("No assigned projects yet.")
        else:
            print("Assigned projects:")
            for project in self.assigned_projects:
                print(project)

    def assign_project(self, project):

        if not isinstance(project, Project):
            raise TypeError("project must be a Project object.")

        self.assigned_projects.append(project)

        print("Project assigned successfully to ", self.name)


    def to_dict(self):
        data = super().to_dict()
        data["skills"] = self.skills
        data["assigned_projects"] = self.assigned_projects
        return data

    @classmethod
    def from_dict(cls, user_id, user_data):
        obj = cls(
            user_id,
            user_data["name"],
            user_data["phone_num"],
            user_data["password"],
            user_data["skills"]
        )
        obj.assigned_projects = user_data["assigned_projects"]
        return obj