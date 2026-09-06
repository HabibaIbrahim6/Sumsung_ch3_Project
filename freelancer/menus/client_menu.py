from ..models.project import Project
from ..models.client import Client


class ClientMenu:

    def __init__(self, client, manager):
        self.client = client
        self.manager = manager

    def show_menu(self):
        """
        Display the client menu and handle client choices.
        """

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

            choice = input("Enter your choice (1-9): ").strip()

            if choice == "1":
                self.create_project()

            elif choice == "2":
                self.client.view_projects()

            elif choice == "3":
                self.search_freelancers()

            elif choice == "4":
                self.send_project_request()

            elif choice == "5":
                self.client.view_requests()

            elif choice == "6":
                self.client.view_messages()

            elif choice == "7":
                self.client.display_profile()

            elif choice == "8":
                self.delete_project()

            elif choice == "9":
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 9.")


    def create_project(self):
        """
        Get project information from the client
        and create a Project object.
        """

        print("\n========== CREATE PROJECT ==========")

        project_id = input("Enter project ID: ").strip()
        title = input("Enter project title: ").strip()
        description = input("Enter project description: ").strip()

        # Validate budget
        try:
            budget = float(input("Enter project budget: ").strip())

            if budget <= 0:
                print("Budget must be greater than zero.")
                return

        except ValueError:
            print("Invalid budget. Please enter a number.")
            return

        deadline = input("Enter project deadline: ").strip()

        try:

            # Create Project object
            project = Project(
                project_id,
                title,
                description,
                budget,
                self.client,
                deadline # type: ignore
            )

            # Use the method already implemented in Client
            self.client.create_project(project)

        except (ValueError, TypeError) as error:
            print(f"Error: {error}")

    

    def view_projects(self):
        """
        Display projects created by the client.
        """

        self.client.view_projects()

    

    def search_freelancers(self):
      pass

    def send_project_request(self):
        """
        Send a project request from the client to a freelancer.
        """

        print("\n========== SEND PROJECT REQUEST ==========")

        # Check if client has projects
        if not self.client.projects_created:
            print("You have no projects.")
            print("Please create a project first.")
            return

        # Display client's projects
        self.client.view_projects()

        project_id = input(
            "\nEnter the project ID: "
        ).strip()

        project = self.client.get_project_by_id(project_id)

        if project is None:
            print("Project not found.")
            return

        # Display freelancers
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

   
    def view_requests(self):
        """
        Display all project requests sent by the client.
        """

        self.client.view_requests()
        

    def view_messages(self):
        """
        Display messages received by the client.
        """

        self.client.view_messages()


    def view_profile(self):
        """
        Display the client's profile.
        """

        self.client.display_profile()

  

    def delete_project(self):
        """
        Delete a project created by the client.
        """

        print("\n========== DELETE PROJECT ==========")

        if not self.client.projects_created:
            print("You have no projects to delete.")
            return

        self.client.view_projects()

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

        self.client.delete_project(project_id)

