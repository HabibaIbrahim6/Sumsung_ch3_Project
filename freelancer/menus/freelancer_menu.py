from ..models.project import Project
from ..models.freelancer import Freelancer
from ..utils import validators as val
from ..utils import helper_functions
from ..models.freelancemaneger import FreelanceManager


class FreelancerMenu:

    def __init__(self, freelancer:Freelancer, manager:FreelanceManager):
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
            print("4. View Messages")
            print("5. Financial Report")
            print("6. View Profile")
            print("7. Edit Profile")
            print("8. Logout")
            print("=================================")

            choice = helper_functions.get_menu_choice(1, 8)

            if choice == 1:
                self.view_assigned_projects()

            elif choice == 2:
                self.update_milestone_status()

            elif choice == 3:
                self.view_and_respond_to_requests()

            elif choice == 4:
                self.view_messages() #pass 

            elif choice == 5:
                self.financial_report()

            elif choice == 6:
                self.view_profile()

            elif choice == 7:
                self.edit_profile()

            elif choice == 8:
                print("Logged out successfully.")
                break

    def view_assigned_projects(self):
        for project in self.freelancer.assigned_projects:
            print(f"Project ID: {project.project_id}, Title: {project.title}, Status: {project.status}")
        
        
    def update_milestone_status(self):
        
        project = self.freelancer.get_project_by_id(input("Enter project ID: "))
        if project is None:
            print("Project ID not found.")

        else:
            project.print_milestones()

            milestone_choice = helper_functions.get_menu_choice(1, len(project.milestones),"Choose milestone to update")

            current_milestone = project.milestones[milestone_choice - 1]
            new_status = helper_functions.get_new_milestone_status()
            current_milestone.update_status(new_status)
            project.update_project_status()
            self.freelancer.save_updated_project(project)  
            self.manager.save_users()  
            
    def view_and_respond_to_requests(self):
        pending_requests = [
            request for request in self.freelancer.received_requests
            if request["status"] == "pending"
        ]

        if not pending_requests:
            print("No pending requests.")
            return

        for request in pending_requests:
            print(
                f"Request from Client: {request['client'].name}, "
                f"Project: {request['project'].title}, "
                f"Message: {request['message']}"
            )

            decision = input(
                "Do you want to accept or reject request (accept/reject): "
            ).strip().lower()

            while decision not in ["accept", "reject"]:
                decision = input(
                    "Invalid choice. Please choose 'accept' or 'reject': "
                ).strip().lower()

            if decision == "accept":
                self.freelancer.assign_project(request["project"])
                request["status"] = "accepted"
                print("Request accepted and project assigned.")
            else:
                request["status"] = "rejected"
                print("Request rejected.")
            self.manager.save_users()  
    def view_messages(self):
        pass
    def financial_report(self):
        print("========== FINANCIAL REPORT ==========")

        invoiced_projects = [
            project for project in self.freelancer.assigned_projects
            if project.invoice is not None
        ]

        if not invoiced_projects:
            print("No invoices yet.")
            return

        total_amount = 0
        total_commission = 0
        total_earnings = 0

        for project in invoiced_projects:
            invoice = project.invoice

            print(f"\nProject: {project.title}")
            print(f"  Invoice ID: {invoice.invoice_id}")
            print(f"  Status: {invoice.status}")
            print(f"  Total Amount: ${invoice.amount:.2f}")
            print(f"  Platform Commission: ${invoice.platform_commission:.2f}")
            print(f"  Net Earnings: ${invoice.freelancer_earnings:.2f}")

            total_amount += invoice.amount
            total_commission += invoice.platform_commission
            total_earnings += invoice.freelancer_earnings

        print("\n========== SUMMARY ==========")
        print(f"Total Projects: {len(invoiced_projects)}")
        print(f"Total Amount Invoiced: ${total_amount:.2f}")
        print(f"Total Commission Deducted: ${total_commission:.2f}")
        print(f"Total Net Earnings: ${total_earnings:.2f}")

    def view_profile(self):
        self.freelancer.display_profile()

    def edit_profile(self):
        pass