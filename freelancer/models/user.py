import json

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
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "password": self._password,
            "role": self.role,
        }
        
    def update_profile(self, name=None, email=None, password=None): #validation must happen before this function is called
        if name is not None:
            self.name = name

        if email is not None:
            self.email = email

        if password is not None:
            self._password = password
    
class Client(User):
    def __init__(self, user_id, name, phone_num, password):
        super().__init__(user_id, name, phone_num, password, "Client")
        self.projects_created = []

    def display_profile(self):
        super().display_profile()

        if not self.projects_created:
            print("No projects created yet.")
        else:
            print("Projects created:")
            for project in self.projects_created:
                print(project)
    def to_dict(self):
        data = super().to_dict()
        data["projects_created"] = self.projects_created
        return data

    @classmethod
    def from_dict(cls, user_id, user_data):
        obj = cls(
            user_id,
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        obj.projects_created = user_data["projects_created"]
        return obj      
