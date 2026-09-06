class User:

    def __init__(self, user_id, name, email, password, role):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def check_password(self, password):
        """
        Check if the entered password matches
        the user's password.
        """

        return self.password == password

    def display_profile(self):
        """
        Display basic user information.
        """

        print("\n========== PROFILE ==========")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Role: {self.role}")

    def to_dict(self):
        """
        Convert user information to dictionary
        for JSON storage.
        """

        return {
            "user_id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "role": self.role
        }
