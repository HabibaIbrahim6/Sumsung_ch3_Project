class Project:
    def __init__(self, project_id, title, budget, client, deadline):
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

    def update_status(self):
        if self.milestones:
            if all(milestone.status == "Completed" for milestone in self.milestones):
                self.status = "Completed"
            elif any(milestone.status == "In Progress" for milestone in self.milestones):
                self.status = "In Progress"

    def update_milestone_status(self, milestone_id, new_status):
        for milestone in self.milestones:
            if milestone.id == milestone_id:
                milestone.update_status(new_status)
                self.update_status()
                return