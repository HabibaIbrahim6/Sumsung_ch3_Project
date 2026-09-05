import json
from .user import Client, Freelancer
from .project import Project
from .invoice import Invoice

class FreelanceManager:
    def __init__(self):
        self.clients = []
        self.freelancers = []
        self.projects = []
        self.invoices = []

        self._client_counter = 1
        self._freelancer_counter = 1
        self._project_counter = 1
        self._invoice_counter = 1
        
        
