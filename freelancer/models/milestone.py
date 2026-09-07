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

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "deadline": self.deadline
        }

    @classmethod
    def from_dict(cls, milestone_data):

        milestone = cls(
            milestone_data["title"],
            milestone_data["description"],
            milestone_data["deadline"]
        )

        milestone.status = milestone_data.get(
            "status",
            "Pending"
        )

        return milestone