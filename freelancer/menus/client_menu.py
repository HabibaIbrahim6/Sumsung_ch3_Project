from ..models.project import Project
from ..models.client import Client
from ..utils import validators as val
from ..utils import helper_functions


class ClientMenu:

    def __init__(self, client, manager):
        self.client = client
        self.manager = manager

    # =========================================================
    # MAIN MENU
    # =========================================================

    def show_menu(self):

        while True:

            print("\n=================================")
            print("          CLIENT MENU")
            print("=================================")
            print("1. Create Project")
            print("2. View My Projects")
            print("3. Search Freelancers")
            print("4. Send Project Request")
            print("5. View Sent Requests")
            print("6. View Messages")
            print("7. View Profile")
            print("8. Delete Project")
            print("9. Logout")
            print("=================================")

            choice = helper_functions.get_menu_choice(1, 9)

            if choice == 1:
                self.create_project()

            elif choice == 2:
                self.view_projects()

            elif choice == 3:
                self.search_freelancers()

            elif choice == 4:
                self.send_project_request()

            elif choice == 5:
                self.view_requests()

            elif choice == 6:
                self.view_messages()

            elif choice == 7:
                self.view_profile()

            elif choice == 8:
                self.delete_project()

            elif choice == 9:
                print("Logged out successfully.")
                break

    # =========================================================
    # CREATE PROJECT
    # =========================================================

    def create_project(self):

        print("\n========== CREATE PROJECT ==========")

        # Generate ID automatically
        project_id = helper_functions.generate_id(
            "P",
            len(self.manager.projects) + 1
        )

        print(f"Generated Project ID: {project_id}")

        # -----------------------------
        # Title validation
        # -----------------------------

        while True:

            title = input("Enter project title: ").strip()

            if title:
                break

            print("Title cannot be empty.")

        # -----------------------------
        # Description validation
        # -----------------------------

        while True:

            description = input(
                "Enter project description: "
            ).strip()

            if description:
                break

            print("Description cannot be empty.")

        # -----------------------------
        # Budget validation
        # -----------------------------

        while True:

            budget_input = input(
                "Enter project budget: "
            ).strip()

            if val.is_valid_amount(budget_input):
                budget = float(budget_input)
                break

            print(
                "Invalid budget. "
                "Please enter a number greater than 0."
            )

        # -----------------------------
        # Deadline validation
        # -----------------------------

        while True:

            deadline = input(
                "Enter project deadline (YYYY-MM-DD): "
            ).strip()

            if val.is_valid_date(deadline):
                break

            print(
                "Invalid deadline. "
                "Use YYYY-MM-DD format."
            )

        # -----------------------------
        # Create Project
        # -----------------------------

        try:

            project = Project(
                project_id,
                title,
                description,
                budget,
                self.client
            )

            project.deadline = deadline

            self.client.create_project(project)
            self.manager.save_users()

            self.manager.projects.append(project)

            print("\nProject created successfully!")
            print(f"Project ID: {project_id}")

        except (ValueError, TypeError, AttributeError) as error:

            print(f"Error: {error}")

    # =========================================================
    # VIEW PROJECTS
    # =========================================================

    def view_projects(self):

        self.client.view_projects()

    # =========================================================
    # SEARCH FREELANCERS
    # =========================================================

    def search_freelancers(self):

        print("\n========== FREELANCERS ==========")

        freelancers = [
            user
            for user in self.manager.users.values()
            if user.role == "Freelancer"
        ]

        if not freelancers:
            print("No freelancers available.")
            return

        for freelancer in freelancers:

            skills = getattr(freelancer, "skills", [])

            if isinstance(skills, list):
                skills = ", ".join(skills)

            print(
                f"ID: {freelancer.id} | "
                f"Name: {freelancer.name} | "
                f"Skills: {skills}"
            )

    # =========================================================
    # SEND PROJECT REQUEST
    # =========================================================

    def send_project_request(self):

        print("\n========== SEND PROJECT REQUEST ==========")

        if not self.client.projects_created:

            print("You have no projects.")
            print("Please create a project first.")
            return

        self.client.view_projects()

        project_id = input(
            "\nEnter project ID: "
        ).strip()

        project = self.client.get_project_by_id(project_id)

        if project is None:

            print("Project not found.")
            return

        self.search_freelancers()

        freelancer_id = input(
            "\nEnter freelancer ID: "
        ).strip()

        message = input(
            "Enter your message: "
        ).strip()

        try:

            request = self.manager.send_project_request(
                client=self.client,
                project=project,
                freelancer_id=freelancer_id,
                message=message
            )

            self.client.add_request(request)

            print("Project request sent successfully.")

        except (ValueError, TypeError) as error:

            print(f"Error: {error}")

    # =========================================================
    # VIEW REQUESTS
    # =========================================================

    def view_requests(self):

        self.client.view_requests()

    # =========================================================
    # VIEW MESSAGES
    # =========================================================

    def view_messages(self):

        self.client.view_messages()

    # =========================================================
    # VIEW PROFILE
    # =========================================================

    def view_profile(self):

        self.client.display_profile()

    # =========================================================
    # DELETE PROJECT
    # =========================================================

    def delete_project(self):

        print("\n========== DELETE PROJECT ==========")

        if not self.client.projects_created:

            print("You have no projects to delete.")
            return
        # View the client's projects to help them choose which one to delete
        self.client.view_projects()
       
        #strip() is used to remove any leading or trailing whitespace from the input, ensuring that the project ID is clean and accurate for the lookup.
        project_id = input(
            "\nEnter project ID to delete: "
        ).strip()

        project = self.client.get_project_by_id(project_id)

        if project is None:

            print("Project not found.")
            return

        confirmation = input(
            "Are you sure you want to delete this project? (y/n): "
        ).strip().lower()

        if confirmation != "y":
            print("Delete cancelled.")
            return
        # The following line calls the delete_project method of the client instance. This method attempts to remove the project with the specified project_id from the client's list of created projects. If the deletion is successful, it returns True; otherwise, it returns False.
        if self.client.delete_project(project_id):
            self.manager.save_users()
            print("Project deleted from saved data.")

        # Remove it from manager too
        if project in self.manager.projects:
            self.manager.projects.remove(project)