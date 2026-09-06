from ..models.project import Project
from ..models.freelancer import Freelancer
from ..utils import validators as val
from ..utils import helper_functions
from ..models.freelancemaneger import FreelancerManager


class FreelancerMenu:

    def __init__(self, freelancer:Freelancer, manager:FreelancerManager):
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
                self.view_messages()

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

            milestone_choice = helper_functions.get_menu_choice(1, len(project.milestones),
                                                                "Choose milestone to update")

            current_milestone = project.milestones[milestone_choice - 1]
            new_status = helper_functions.get_new_milestone_status()
            current_milestone.update_status(new_status)
            project.update_project_status()
            self.freelancer.save_updated_project(project)  
            self.manager.save_users()  
            
    def view_and_respond_to_requests(self):
        for request in self.freelancer.received_requests:
            if request["status"] == "pending":
                print(f"Request from Client: {request['client'].name}, Project: {request['project'].title}, Message: {request['message']}")
                decision = input("Do you want to accept or reject request (accept/reject): ").strip().lower()
                while decision not in ["accept", "reject"]:
                    if decision == "accept":
                        self.freelancer.assign_project(request["project"])
                        request["status"] = "accepted"
                        print("Request accepted and project assigned.")
                    elif decision == "reject":
                        request["status"] = "rejected"
                        print("Request rejected.")
                    else:
                        print("Invalid choice. Please choose 'accept' or 'reject'.")

    def view_messages(self):
        pass
    def financial_report(self):
        pass

    def view_profile(self):
        self.freelancer.display_profile()

    def edit_profile(self):
        pass