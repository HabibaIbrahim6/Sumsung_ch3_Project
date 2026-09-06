class Proposal:
    def __init__(
        self,
        proposal_id,
        project,
        freelancer,
        client,
        price,
        message
    ):
        self.id = proposal_id
        self.project = project
        self.freelancer = freelancer
        self.client = client
        self.price = price
        self.message = message
        self.status = "Pending"