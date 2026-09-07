from models.invoice import Invoice
from ..models.project import Project
from ..models.client import Client
from ..utils import validators as val
from ..utils import helper_functions
from ..models.freelancemaneger import FreelanceManager
from ..models.freelancer import Freelancer 
class ClientMenu:

    def __init__(self, client: Client, manager: FreelanceManager, freelancer: Freelancer,invoice: Invoice):
        self.client = client
        self.manager = manager
        self.freelancer = freelancer
        self.invoice = invoice


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
            print("8. Update Milestones")
            print("9. Generate Invoice")
            print("10. Delete Project")
            print("11. Logout")
            print("=================================")

            choice = helper_functions.get_menu_choice(1, 11)

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
                self.update_milestones()

            elif choice == 9:
                self.generate_invoice()

            elif choice == 10:
                self.delete_project()

            elif choice == 11:
                print("Logged out successfully.")
                break


    def create_project(self):

        print("\n========== CREATE PROJECT ==========")

        project_id = helper_functions.generate_id(
            "P",
            len(self.manager.projects) + 1
        )

        print(f"Generated Project ID: {project_id}")

        title = val.get_valid_title("Enter project title: ")

        budget = val.get_valid_amount("Enter the project budget: ")

        deadline = val.get_valid_deadline("Enter the project deadline YYYY-MM-DD: ")

        milestones = helper_functions.get_milestones()

        project = Project(
            project_id,
            title,
            budget,
            self.client,
            deadline,
            milestones
        )

        invoice = Invoice(helper_functions.generate_id("INV", 1), project_id,budget)
        project.add_invoice(invoice)    
        self.client.add_project(project)

        print("\nProject created successfully")
        print(f"Project ID: {project_id}")

        


    def view_projects(self):

        self.client.view_projects()


    def search_freelancers(self):

        print("\n========== FREELANCERS ==========")

        print("1. all freelancers")
        print("2. freelancers by skill")
        print("3. freelancers by project count done")
        
        choice = helper_functions.get_menu_choice(1, 3)
        if choice == 1:
            freelancers = [
                user
                for user in self.manager.users.values()
                if user.role == "Freelancer"
            ]
        elif choice == 2:
            skill = input("Enter skill to search for: ").strip()
            freelancers = [
                user
                for user in self.manager.users.values()
                if user.role == "Freelancer" and skill in getattr(user, "skills", [])
            ]
        elif choice == 3:
            freelancers = [
                user
                for user in self.manager.users.values()
                if user.role == "Freelancer"
            ]
            freelancers.sort(key=lambda x: len(x.projects_done), reverse=True)

        if not freelancers:
            print("No freelancers found")
            return

        for freelancer in freelancers:

            skills = getattr(freelancer, "skills", [])

            if isinstance(skills, list):
                skills = "- ".join(skills)

            print(
                f"ID: {freelancer.id}  "
                f"Name: {freelancer.name} "
                f"Skills: {skills}"
                "---------"
            )


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

        request = {"client":self.client,
                        "project":project,
                        "freelancer_id":freelancer_id,
                        "message":message,
                        "status": "pending"
                        }
            
        self.freelancer.add_request(request)
        self.client.add_request(request)
        print("Project request sent successfully.")

    def view_requests(self):
        self.client.view_requests()


    def view_messages(self):

        self.client.view_messages()

 
    def view_profile(self):

        self.client.display_profile()

  
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


    def update_milestones(self):
        print("\n========== UPDATE MILESTONES ==========")
        print("Enter the project ID:")
        project_id = input()
        current_project = self.client.get_project_by_id(project_id)

        if current_project is None:
            print("Project ID not found.")

        else:
            current_project.print_milestones()

            milestone_choice = helper_functions.get_menu_choice(1, len(current_project.milestones),
                                                                "Choose milestone to update")

            current_milestone = current_project.milestones[milestone_choice - 1]
            new_status = helper_functions.get_new_milestone_status()
            current_milestone.update_status(new_status)
            current_project.update_project_status()


    def generate_invoice(self):
        print("\n========== GENERATE INVOICE ==========")
        candidate_projects = helper_functions.create_list_of_candidate_projects_for_invoicing(self.client)
        if not candidate_projects:
            print("There are no projects available for invoicing.")
        else:

            helper_functions.print_menu(candidate_projects)

            choice = helper_functions.get_menu_choice(1, len(candidate_projects), "Choose a project to invoice")

            project = candidate_projects[choice - 1]
            invoice_id = helper_functions.generate_id("INV",1) #1 is a placeholder till I  find a solution
            invoice = Invoice(invoice_id, project.id, project.budget)
            project.invoice = invoice
            print("\n========== INVOICE GENERATED SUCCESSFULLY ==========")
            invoice.display_invoice()
