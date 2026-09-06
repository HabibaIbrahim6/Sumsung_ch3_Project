class Project:
    def __init__(self,project_id, title, budget, client, deadline):
        self.id = project_id
        self.title = title
        self.budget = budget
        self.client = client
        self.freelancer = None
        self.status = "Open"
        self.deadline = deadline
        self.milestones = []

    def __str__(self):
        return f"Project ID: {self.id} , Title: {self.title} , Status: {self.status}"

    def update_project_status(self):

        if self.milestones:
            if all(milestone.status == "Completed" for milestone in self.milestones):
                self.status = "Completed"
            elif any(milestone.status != "Pending" for milestone in self.milestones):
                self.status = "In Progress"


    def print_milestones(self):
        if not self.milestones:
            print("This project has no milestones.")
            return
        for index, milestone in enumerate(self.milestones, start=1):
            print(f"{index}) {milestone}")


    def assign_freelancer(self, freelancer):
        self.freelancer = freelancer
        self.status = "Assigned"
