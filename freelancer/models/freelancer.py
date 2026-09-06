from .user import User

class Freelancer(User):
    def __init__(self, user_id, name, email, password, portfolio):
        super().__init__(user_id, name, email, password, "Freelancer")
        self.portfolio = portfolio
        self.assigned_projects = []

    def display_profile(self):
        super().display_profile()
        print(f"Portfolio -> {self.portfolio}")

        if not self.assigned_projects:
            print("No assigned projects yet.")
        else:
            print("Assigned projects:")
            for project in self.assigned_projects:
                print(project)