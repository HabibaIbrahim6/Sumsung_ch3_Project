from models.client import Client
from models.project import Project


client = Client(
    "C001",
    "Habiba",
    "habiba@gmail.com",
    "123456"
)

project = Project(
    "P001",
    "E-Commerce Website",
    "Build an online shopping website",
    15000,
    client,
)

client.create_project(project)

client.view_projects()