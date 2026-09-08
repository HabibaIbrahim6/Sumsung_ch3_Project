from ..utils.helper_functions import print_menu
from .invoice import Invoice
from .milestone import Milestone


class Project:

    def __init__(
        self,
        project_id,
        title,
        budget,
        client,
        deadline,
        milestones
    ):
        self.id = project_id
        self.title = title
        self.budget = budget
        self.client = client
        self.freelancer = None
        self.status = "Open"
        self.deadline = deadline
        self.milestones = milestones
        self.invoice = None

    def __str__(self):
        return f"Project ID: {self.id} Title: {self.title} Status: {self.status} "

    def update_project_status(self):

        if not self.milestones:
            return

        if all(milestone.status == "Completed" for milestone in self.milestones):
            self.status = "Completed"

        elif any(milestone.status != "Pending" for milestone in self.milestones):
            self.status = "In Progress"

        else:
            self.status = "Assigned" if self.freelancer else "Open"

    def print_milestones(self):

        if not self.milestones:
            print("This project has no milestones.")
            return

        print_menu(self.milestones)

    def assign_freelancer(self, freelancer):

        self.freelancer = freelancer
        self.status = "Assigned"

    def add_invoice(self, invoice):

        if not isinstance(invoice, Invoice):
            raise TypeError("invoice must be an Invoice object.")

        self.invoice = invoice

    def to_dict(self):

        return {
            "project_id": self.id,
            "title": self.title,
            "budget": self.budget,
            "client": self.client.id
            if self.client else None,
            "freelancer": self.freelancer.id
            if self.freelancer else None,
            "status": self.status,
            "deadline": self.deadline,
            "milestones": [ milestone.to_dict() for milestone in self.milestones ],
            "invoice": (self.invoice.to_dict() if self.invoice else None)
        }
    @classmethod
    def from_dict(cls,project_data,client=None,freelancer=None):

        milestones = [ Milestone.from_dict(milestone_data) for milestone_data in project_data.get("milestones", []) ]

        invoice = None

        if project_data.get("invoice"):
            invoice = Invoice.from_dict(project_data["invoice"])

        project = cls(
            project_id=project_data["project_id"],
            title=project_data["title"],
            budget=project_data["budget"],
            client=client,
            deadline=project_data["deadline"],
            milestones=milestones
        )

        project.freelancer = freelancer

        project.status = project_data.get("status","Open")

        project.invoice = invoice

        return project
