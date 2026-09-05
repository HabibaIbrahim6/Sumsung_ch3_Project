import json

class User:
    def __init__(self, user_id, name, phone_num, password, role):
        self.user_id = user_id
        self.name = name
        self.phone_num = phone_num
        self._password = password
        self.role = role

    def check_password(self, password):
        return self._password == password
    
    def display_profile(self):
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_num}")
        print(f"Role: {self.role}")
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "phone_num": self.phone_num,
            "password": self._password,
            "role": self.role,
        }
        
    def update_profile(self, name=None, phone_num=None, password=None):
        pass
    
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
            user_data["phone_num"],
            user_data["password"]
        )
        obj.projects_created = user_data["projects_created"]
        return obj      

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