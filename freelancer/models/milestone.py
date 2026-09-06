class Milestone:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.status = "Pending"
        self.deadline = deadline

    def __str__(self):
        return f"Title: {self.title} | Status: {self.status}"

    def update_status(self, new_status):
        self.status = new_status