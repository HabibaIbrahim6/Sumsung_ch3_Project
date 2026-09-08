from typing import TYPE_CHECKING

from ..models.freelancer import Freelancer
from ..utils import helper_functions
from ..utils import validators as val
if TYPE_CHECKING:
    from ..models.freelancemaneger import FreelanceManager


class FreelancerMenu:
    def __init__(self,freelancer: Freelancer, manager: "FreelanceManager"):
        self.freelancer = freelancer
        self.manager = manager

  
    def show_menu(self):
        while True:
            print("\n=================================")
            print("        FREELANCER MENU")
            print("=================================")
            print("1. View Assigned Projects")
            print("2. Update Milestone Status")
            print("3. View & Respond to Requests")
            print("4. Financial Report")
            print("5. View Profile")
            print("6. Edit Profile")
            print("7. Logout")
            print("=================================")

            choice = helper_functions.get_menu_choice(1, 7)

            if choice == 1:
                self.view_assigned_projects()

            elif choice == 2:
                self.update_milestone_status()

            elif choice == 3:
                self.view_and_respond_to_requests()

            elif choice == 4:
                self.financial_report()

            elif choice == 5:
                self.view_profile()

            elif choice == 6:
                self.edit_profile()

            elif choice == 7:
                print("Logged out successfully.")
                break


    def view_assigned_projects(self):
        print("========== ASSIGNED PROJECTS ==========")

        if not self.freelancer.assigned_projects:
            print("No assigned projects.")
            return

        for project in self.freelancer.assigned_projects:
            print(f"Project ID: {project.id}")

            print(f"Title: {project.title}")

            print(f"Status: {project.status}")

            print("----------------------------------")

  
    def update_milestone_status(self):
        if not self.freelancer.assigned_projects:
            print("You have no assigned projects.")
            return

        project_id = input("Enter project ID: ").strip()

        project = self.freelancer.get_project_by_id(project_id)

        if project is None:
            print("Project ID not found.")
            return

        if not project.milestones:
            print("This project has no milestones.")
            return

        print(f"Project: {project.title}")
        project.print_milestones()

        milestone_choice = helper_functions.get_menu_choice(1,len(project.milestones),"Choose milestone to update ")

        current_milestone = project.milestones[milestone_choice - 1]

        print(f"Current status:{current_milestone.status}")

        new_status = (helper_functions.get_new_milestone_status())

        current_milestone.update_status(new_status)

        project.update_project_status()

        self.manager.save_users()

        print("Milestone updated successfully.")

        print(f"Project status: {project.status}")

  
    def view_and_respond_to_requests(self):
        pending_requests = (self.freelancer.get_pending_requests())

        if not pending_requests:
            print("No pending requests.")
            return

        print("========== PROJECT REQUESTS ==========")

        for request in pending_requests:
            client = request.get("client")
            project = request.get("project")

            if project.freelancer is not None:
                request["status"] = "cancelled"
                self.manager.save_users()
                continue

            print(f"Client: {client.name}")

            print(f"Project: {project.title}")

            print(f"Message: {request.get('message', '')}")

            decision = input("\nAccept or reject? ").strip().lower()

            while decision not in ["accept","reject"]:

                decision = input("Please enter accept or reject: ").strip().lower()

            if decision == "accept":
                success = (self.freelancer.assign_project(project))

                if success:
                    request["status"] = "accepted"
                    print("Request accepted and project assigned")

            else:
                request["status"] = "rejected"
                print("Request rejected.")

            self.manager.save_users()
  
    def financial_report(self):

        print("========== FINANCIAL REPORT ==========")

        invoiced_projects = [ project for project in self.freelancer.assigned_projects if project.invoice is not None ]

        if not invoiced_projects:
            print("No invoices yet.")
            return

        total_amount = 0
        total_commission = 0
        total_earnings = 0

        for project in invoiced_projects:
            invoice = project.invoice
            print(f"\nProject: {project.title}")

            print(f"Invoice ID:{invoice.invoice_id}")

            print(f"Status: {invoice.status}")

            print(f"Total Amount: ${invoice.amount:.2f}")

            print(f"Platform Commission:${invoice.platform_commission:.2f}")

            print(f"Net Earnings: ${invoice.freelancer_earnings:.2f}")

            total_amount += invoice.amount
            total_commission += invoice.platform_commission
            total_earnings += invoice.freelancer_earnings

        print("========== SUMMARY ==========")

        print(f"Total Projects: {len(invoiced_projects)}")

        print(f"Total Amount Invoiced: ${total_amount:.2f}")

        print(f"Total Commission Deducted: ${total_commission:.2f}")

        print(f"Total Net Earnings: ${total_earnings:.2f}")

   
    def view_profile(self):
        self.freelancer.display_profile()

    def edit_profile(self):
        print("\n========== EDIT PROFILE ==========")
        print("1. Edit Name")
        print("2. Edit Email")
        print("3. Edit Password")
        print("4. Edit Skills")
        print("5. Cancel")

        choice = helper_functions.get_menu_choice(1, 5)

        if choice == 1:
            new_name = input("Enter new name: ").strip()

            if not new_name:
                print("Name cannot be empty.")
                return

            self.freelancer.name = new_name
            print("Name updated.")

        elif choice == 2:
            new_email = input("Enter new email: ").strip()

            if not val.is_valid_email(new_email):
                print("Invalid email format.")
                return

            self.freelancer.email = new_email
            print("Email updated.")

        elif choice == 3:
            new_password = input("Enter new password: ").strip()

            if not val.is_valid_password(new_password):
                print(
                    "Invalid password."
                    "\nPassword must:"
                    "\n- contain at least 9 characters"
                    "\n- contain at least one digit"
                    "\n- contain at least one special character"
                )
                return

            self.freelancer.password = new_password
            print("Password updated.")

        elif choice == 4:
            skills_input = input("Enter skills separated by comma (,): ").strip()

            new_skills = [skill.strip() for skill in skills_input.split(",") if skill.strip()]

            if not new_skills:
                print("Please enter at least one skill.")
                return

            self.freelancer.skills = new_skills
            print("Skills updated.")

        else:
            return

        self.manager.save_users()
