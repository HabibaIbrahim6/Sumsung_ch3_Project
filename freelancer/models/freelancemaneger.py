import json

from .client import Client
from .freelancer import Freelancer
from ..utils import helper_functions


class FreelanceManager:

    def __init__(self):
        self.users = {}  # Dictionary to store users by their ID

        # Load users from data.jsonl
        self.load_users()
      
   
        self.projects = []
   

     
    def load_users(self):
        """
        Load users from data.jsonl and recreate their objects.
        """

        try:

            with open("data.jsonl", "r") as file:

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    user_data = json.loads(line)

                    user_id = user_data["user_id"]

                    # Recreate Client object
                    if user_data["role"] == "Client":

                        user = Client.from_dict(
                            user_id,
                            user_data
                        )

                    # Recreate Freelancer object
                    elif user_data["role"] == "Freelancer":

                        user = Freelancer.from_dict(
                            user_id,
                            user_data
                        )

                    else:
                        continue

                    self.users[user_id] = user

        except FileNotFoundError:
            # File doesn't exist yet
            # It will be created when the first user registers
            return

 
    def append_user(self, user):
        """
        Save a user to data.jsonl.
        """

        with open("data.jsonl", "a") as file:

            file.write(
                json.dumps(user.to_dict()) + "\n"
            )

  
    def login(self, user_id, password):
        """
        Check user credentials and return the logged-in user.
        """

        # Check if user exists
        if user_id not in self.users:

            print("User not found.")
            return None

        user = self.users[user_id]

        # Check password
        if not user.check_password(password):

            print("Wrong password.")
            return None

        print("\nLogin successful!")
        print(f"Welcome, {user.name}!")

        # Return user to MainMenu
        # MainMenu will decide which menu to open
        return user

   
    def register_client(self, name, phone_num, password):
        """
        Create and save a new Client.
        """

        # Generate unique client ID
        user_id = helper_functions.generate_id(
            "C",
            len(self.users) + 1
        )

        # Create Client object
        client = Client(
            user_id,
            name,
            phone_num,
            password
        )

        # Store user in dictionary
        self.users[user_id] = client

        # Save user to JSON
        self.append_user(client)

        print("\nClient registered successfully!")
        print(f"Your User ID is: {user_id}")

        return client

   
    def register_freelancer(
        self,
        name,
        phone_num,
        password,
        skills
    ):
        """
        Create and save a new Freelancer.
        """

        # Generate unique freelancer ID
        user_id = helper_functions.generate_id(
            "F",
            len(self.users) + 1
        )

        # Create Freelancer object
        freelancer = Freelancer(
            user_id,
            name,
            phone_num,
            password,
            skills
        )

        # Store freelancer
        self.users[user_id] = freelancer

        # Save freelancer to JSON
        self.append_user(freelancer)

        print("\nFreelancer registered successfully!")
        print(f"Your User ID is: {user_id}")

        return freelancer

   
    def get_freelancers(self):
        """
        Return all registered freelancers.
        """

        return [
            user
            for user in self.users.values()
            if isinstance(user, Freelancer)
        ]

   
    def get_user_by_id(self, user_id):
        """
        Find a user by their ID.
        """

        return self.users.get(user_id)
    
    def save_users(self):

        with open("data.jsonl", "w") as file:

            for user in self.users.values():

                file.write(
                    json.dumps(user.to_dict()) + "\n"
                )

