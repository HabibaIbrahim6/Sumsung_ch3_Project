from typing import TYPE_CHECKING

from ..models.freelancer import Freelancer
from ..utils import helper_functions

if TYPE_CHECKING:
    from ..models.freelancemaneger import FreelanceManager


class FreelancerMenu:

    def __init__(
        self,
        freelancer: Freelancer,
        manager: "FreelanceManager"
    ):
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

            choice = helper_functions.get_menu_choice(
                1,
                8
            )

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

        print("\n========== ASSIGNED PROJECTS ==========")

        if not self.freelancer.assigned_projects:

            print("No assigned projects.")
            return

        for project in self.freelancer.assigned_projects:

            print(
                f"Project ID: {project.id}"
            )

            print(
                f"Title: {project.title}"
            )

            print(
                f"Status: {project.status}"
            )

            print("----------------------------------")

  
    def update_milestone_status(self):

        if not self.freelancer.assigned_projects:

            print("You have no assigned projects.")
            return

        project_id = input(
            "Enter project ID: "
        ).strip()

        project = self.freelancer.get_project_by_id(
            project_id
        )

        if project is None:

            print("Project ID not found.")
            return

        if not project.milestones:

            print("This project has no milestones.")
            return

        print(
            f"\nProject: {project.title}"
        )

        project.print_milestones()

        milestone_choice = helper_functions.get_menu_choice(
            1,
            len(project.milestones),
            "Choose milestone to update "
        )

        current_milestone = project.milestones[
            milestone_choice - 1
        ]

        print(
            f"\nCurrent status: "
            f"{current_milestone.status}"
        )

        new_status = (
            helper_functions
            .get_new_milestone_status()
        )

        current_milestone.update_status(
            new_status
        )

        # Update project status
        project.update_project_status()

        # Save changes
        self.manager.save_users()

        print(
            "\nMilestone updated successfully."
        )

        print(
            f"Project status: {project.status}"
        )

  
    def view_and_respond_to_requests(self):

        pending_requests = (
            self.freelancer.get_pending_requests()
        )

        if not pending_requests:

            print("No pending requests.")
            return

        print(
            "\n========== PROJECT REQUESTS =========="
        )

        for request in pending_requests:

            client = request.get("client")
            project = request.get("project")

            print(
                f"\nClient: {client.name}"
            )

            print(
                f"Project: {project.title}"
            )

            print(
                f"Message: "
                f"{request.get('message', '')}"
            )

            decision = input(
                "\nAccept or reject? "
            ).strip().lower()

            while decision not in [
                "accept",
                "reject"
            ]:

                decision = input(
                    "Please enter accept or reject: "
                ).strip().lower()

            if decision == "accept":

                success = (
                    self.freelancer
                    .assign_project(project)
                )

                if success:

                    request["status"] = "accepted"

                    print(
                        "Request accepted "
                        "and project assigned."
                    )

            else:

                request["status"] = "rejected"

                print(
                    "Request rejected."
                )

            self.manager.save_users()

  
    def view_messages(self):

        print("\n========== MESSAGES ==========")
        print("No messages yet.")

  
    def financial_report(self):

        print(
            "\n========== FINANCIAL REPORT =========="
        )

        invoiced_projects = [
            project
            for project in self.freelancer.assigned_projects
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

            print(
                f"\nProject: {project.title}"
            )

            print(
                f"Invoice ID: "
                f"{invoice.invoice_id}"
            )

            print(
                f"Status: "
                f"{invoice.status}"
            )

            print(
                f"Total Amount: "
                f"${invoice.amount:.2f}"
            )

            print(
                f"Platform Commission: "
                f"${invoice.platform_commission:.2f}"
            )

            print(
                f"Net Earnings: "
                f"${invoice.freelancer_earnings:.2f}"
            )

            total_amount += invoice.amount
            total_commission += (
                invoice.platform_commission
            )
            total_earnings += (
                invoice.freelancer_earnings
            )

        print(
            "\n========== SUMMARY =========="
        )

        print(
            f"Total Projects: "
            f"{len(invoiced_projects)}"
        )

        print(
            f"Total Amount Invoiced: "
            f"${total_amount:.2f}"
        )

        print(
            f"Total Commission Deducted: "
            f"${total_commission:.2f}"
        )

        print(
            f"Total Net Earnings: "
            f"${total_earnings:.2f}"
        )

   
    def view_profile(self):

        print(
            "\n========== PROFILE =========="
        )

        self.freelancer.display_profile()

    def edit_profile(self):

        print(
            "\n========== EDIT PROFILE =========="
        )

        print(
            "Edit profile feature is not implemented yet."
        )