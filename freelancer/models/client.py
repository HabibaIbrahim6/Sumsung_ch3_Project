from .user import User

class Client(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password, "Client")
        self.projects_created = []

    def display_profile(self):
        super().display_profile()

        if not self.projects_created:
            print("No projects created yet.")
        else:
            print("Projects created:")
            for project in self.projects_created:
                print(project)