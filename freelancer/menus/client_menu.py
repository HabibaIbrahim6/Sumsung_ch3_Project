from typing import TYPE_CHECKING

from ..models.invoice import Invoice
from ..models.project import Project
from ..models.client import Client
from ..utils import validators as val
from ..utils import helper_functions


if TYPE_CHECKING:
    from ..models.freelancemaneger import FreelanceManager


class ClientMenu:

    def __init__(self, client: Client, manager: "FreelanceManager"):
        self.client = client
        self.manager = manager

   

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
            print("6. View Profile")
            print("7. Update Milestones")
            print("8. Generate Invoice")
            print("9. Delete Project")
            print("10. Logout")
            print("=================================")

            choice = helper_functions.get_menu_choice(1, 10)

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
                self.view_profile()

            elif choice == 7:
                self.update_milestones()

            elif choice == 8:
                self.generate_invoice()

            elif choice == 9:
                self.delete_project()

            elif choice == 10:
                print("Logged out successfully.")
                break

    def create_project(self):

        print("========== CREATE PROJECT ==========")

        project_id = self.manager.next_id("P")

        title = val.get_valid_title("Enter project title: ")

        budget = val.get_valid_amount("Enter the project budget:  ")

        deadline = val.get_valid_deadline("Enter the project deadline DD/MM/YYYY:  ")

        milestones = helper_functions.get_milestones()

        project = Project(
            project_id,
            title,
            budget,
            self.client,
            deadline,
            milestones
        )

        self.client.add_project(project)

        self.manager.add_project(project)

        self.manager.save_users()

        print("\nProject created successfully.")
        print(f"Project ID: {project_id}")

 
    def view_projects(self):

        self.client.view_projects()

 
    def search_freelancers(self):

        print("\n========== FREELANCERS ==========")

        print("1. All freelancers")
        print("2. Freelancers by skill")
        print("3. Freelancers by completed project count")

        choice = helper_functions.get_menu_choice(1, 3)

        freelancers = []

        if choice == 1:
            freelancers = [user for user in self.manager.users.values() if user.role == "Freelancer"]

        elif choice == 2:

            skill = input("Enter skill to search for: ").strip()

            freelancers = [
                user
                for user in self.manager.users.values()
                if user.role == "Freelancer"
                and skill.lower() in [s.lower()for s in getattr(user, "skills", [])]
                ]

        elif choice == 3:

            freelancers = [user for user in self.manager.users.values()if user.role == "Freelancer"]

            freelancers.sort(key=lambda freelancer: len(freelancer.get_completed_projects()),reverse=True)

        if not freelancers :
            print("No freelancers found")
            return

        print("\n========== SEARCH RESULTS ==========")

        for freelancer in freelancers:

            skills = getattr(freelancer,"skills",[])

            if isinstance(skills, list):
                skills_text = ", ".join(skills)
            else:
                skills_text = str(skills)

            projects_done = len(freelancer.get_completed_projects()) #retuned the num of projects not the projects themselves

            print(
                f"ID: {freelancer.id}\n"
                f"Name: {freelancer.name}\n"
                f"Skills: {skills_text}\n"
                f"Completed Projects: {projects_done}"
            )

            print("---------------------------------")


    def send_project_request(self):

        print("========== SEND PROJECT REQUEST ==========")


        if not self.client.projects_created:

            print("You have no projects.")
            print("Please create a project first.")

            return

    

        self.client.view_projects()

        project_id = input("\nEnter project ID: ").strip()

        project = self.client.get_project_by_id(project_id)

        if project is None:

            print("Project not found.")

            return

     
        freelancers = [ user for user in self.manager.users.values() if user.role == "Freelancer" ]

        if not freelancers:

            print("No freelancers available.")

            return

        print("========== AVAILABLE FREELANCERS ==========")

        for freelancer in freelancers:

            skills = getattr(freelancer,"skills",[])

            if isinstance(skills, list):
                skills = "- ".join(skills)

            print(
                f"ID: {freelancer.id} - "
                f"Name: {freelancer.name} -  "
                f"Skills: {skills}"
            )

     

        freelancer_id = input("\nEnter freelancer ID: ").strip()

        freelancer = self.manager.users.get(freelancer_id)

        if freelancer is None or freelancer.role != "Freelancer":

            print("Freelancer not found.")

            return

       

        if project.freelancer is not None:
            print("Project is already assigned.")
            return

        if any(r.get("project") is project and r.get("status") == "pending"
               for r in freelancer.received_requests):
            print("A pending request already exists for this freelancer.")
            return

        message = input("Enter your message: ").strip()

        if not message:

            print("Message cannot be empty.")

            return

       
        request = {
            "client": self.client,
            "project": project,
            "freelancer_id": freelancer.id,
            "message": message,
            "status": "pending"
        }
        freelancer.add_request(request)

        self.client.add_request(request)

        self.manager.save_users()

        print("\nProject request sent successfully.")

 
    def view_requests(self):

        self.client.view_requests()

   
    def view_profile(self):

        print("\n========== MY PROFILE ==========")

        self.client.display_profile()

   
    def delete_project(self):


        if not self.client.projects_created:

            print("You have no projects to delete.")

            return

    
        self.client.view_projects()

        project_id = input(
            "\nEnter project ID to delete: "
        ).strip()

        project = self.client.get_project_by_id(
            project_id
        )

        if project is None:

            print("Project not found.")

            return

        confirmation = input(
            "Are you sure you want to delete this project? (y/n): "
        ).strip().lower()

        if confirmation != "y":

            print("Delete cancelled.")

            return

      
        deleted = self.manager.delete_project(project)

        if deleted:

            self.manager.save_users()

            print("Project deleted successfully.")

   
    def update_milestones(self):

        print("\n========== UPDATE MILESTONES ==========")

        project_id = input(
            "Enter the project ID: "
        ).strip()

        current_project = self.client.get_project_by_id(
            project_id
        )

        if current_project is None:

            print("Project ID not found.")

            return

       
        if not current_project.milestones:

            print("This project has no milestones.")

            return

       
        current_project.print_milestones()

        milestone_choice = helper_functions.get_menu_choice(
            1,
            len(current_project.milestones),
            "Choose milestone to update "
        )

        current_milestone = current_project.milestones[
            milestone_choice - 1
        ]

       
        new_status = helper_functions.get_new_milestone_status()

        current_milestone.update_status(
            new_status
        )



        current_project.update_project_status()


        self.manager.save_users()

        print("\nMilestone status updated successfully.")

    

    def generate_invoice(self):

        print("\n========== GENERATE INVOICE ==========")

        candidate_projects = (
            helper_functions
            .create_list_of_candidate_projects_for_invoicing(
                self.client
            )
        )

        if not candidate_projects:

            print(
                "There are no projects available for invoicing."
            )

            return


        helper_functions.print_menu(
            candidate_projects
        )


        choice = helper_functions.get_menu_choice(
            1,
            len(candidate_projects),
            "Choose a project to invoice "
        )

        project = candidate_projects[
            choice - 1
        ]

        invoice_id = self.manager.next_id("INV")

        invoice = Invoice(
            invoice_id,
            project.id,
            project.budget
        )

        project.add_invoice(invoice)


        print(
            "\n========== INVOICE GENERATED SUCCESSFULLY =========="
        )

        invoice.display_invoice()


        self.manager.save_users()
