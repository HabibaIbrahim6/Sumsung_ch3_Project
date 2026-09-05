class Milestone:
    def __init__(self, milestone_id, title, deadline):
        self.id = milestone_id
        self.title = title
        self.status = "Pending"
        self.deadline = deadline

    def __str__(self):
        return f"Milestone ID: {self.id} , Title: {self.title} , Status: {self.status}"

    def update_status(self, new_status):
        self.status = new_status