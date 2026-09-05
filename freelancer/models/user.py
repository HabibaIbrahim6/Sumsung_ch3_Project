class User:
    def __init__(self, user_id, name, email, password, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self._password = password
        self.role = role

    def check_password(self, password):
        return self._password == password
    
    def display_profile(self):
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Role: {self.role}")

    def update_profile(self, name=None, email=None, password=None):
        pass

    def __str__(self): 
        pass
    
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