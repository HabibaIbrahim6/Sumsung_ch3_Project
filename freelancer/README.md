# Freelancer Project Hub

A Python command-line freelance management system for managing clients, freelancers, projects, milestone tracking, project requests, and basic financial reporting.

This project is designed as a learning/demo application for handling the core operations of a freelance marketplace from the command line.

## Overview

The system allows two main user types to interact with the platform:

- Client: creates projects, searches for freelancers, sends requests, tracks milestones, and manages invoices.
- Freelancer: registers skills, receives project requests, accepts or rejects work, updates milestone progress, and reviews financial summaries.

The app uses a simple in-memory/user-file model with JSON persistence through a `data.json` file.

## Main Features

### 1. User registration and login
- Register as a client
- Register as a freelancer
- Login with a user ID and password
- Basic validation for email and password strength

### 2. Client-side project management
- Create project records
- Set project title, budget, deadline, and milestones
- View created projects
- Delete projects
- Search freelancers by name/skill/projects_completed

### 3. Freelancer discovery and requests
- Client can browse freelancers
- Search by all freelancers or by skill 
- Send a project request to a selected freelancer
- Freelancer can view and accept or reject incoming requests

### 4. Milestone tracking
- Projects can include multiple milestones
- Freelancers can update milestone status
- Project status changes based on milestone completion

### 5. Financial tracking
- Generate invoice data for project budgets
- View platform commission and freelancer earnings
- Review a basic financial report for assigned projects

### 6. Messaging / communication flow
- The project includes request structures for communication between clients and freelancers.
- Messages and requests are stored within user data structures and can be viewed from the menus.

## Project Structure

```text
freelancer/
├── main.py                 # App entry point
├── README.md               # Project documentation
Project
├── models/
│   ├── client.py           # Client model
│   ├── freelancer.py       # Freelancer model
│   ├── freelancemaneger.py # Central app manager
│   ├── invoice.py          # Invoice logic
│   ├── milestone.py        # Milestone tracking
│   ├── project.py          # Project model
│   ├── user.py             # Shared user base class
├── menus/
│   ├── client_menu.py      # Client operations menu
│   ├── freelancer_menu.py  # Freelancer operations menu
│   └── main_menu.py        # Login/registration entry menu
├── utils/
│   ├── helper_functions.py # Shared helper methods
│   └── validators.py       # Input validation rules
└── data.json             # Persistent user data file generated at runtime
```

## Core Classes

### User
Base class for all users. It stores the common attributes:
- user ID
- name
- email
- password
- role

### Client
Represents a client account and includes:
- list of projects created
- sent requests
- messages received
- profile information and data serialization helpers

### Freelancer
Represents a freelancer account and includes:
- skills
- assigned projects
- received requests
- project completion history
- profile and project-tracking methods

### Project
Represents a freelance job or contract and includes:
- project ID
- title
- budget
- client
- assigned freelancer
- status
- deadline
- milestones
- invoice

### Invoice
Stores invoice details such as:
- invoice ID
- project ID
- total amount
- platform commission
- freelancer net earnings
- status

## Workflow

### Client workflow
1. Register as a client.
2. Log in.
3. Create a project with a budget and deadline.
4. Add milestone breakdowns.
5. Search and contact freelancers.
6. Send project requests.
7. Track project progress and invoices.
8. Delete projects when needed.

### Freelancer workflow
1. Register as a freelancer.
2. Add your skills.
3. Log in.
4. Review incoming project requests.
5. Accept or reject offers.
6. View assigned projects.
7. Update milestone statuses.
8. Review financial report and earnings.

## Requirements

This project uses Python 3 and standard library features only.

Recommended:
- Python 3.10+
- Terminal/command prompt

## Running the Application

From the repository root, run:

```bash
python -m freelancer.main
```

This starts the interactive menu system.

If you are already inside the `freelancer` folder, the project is structured to be launched with the package-style module entry point as well

Because this project uses relative imports, the module-style launch is the safest option.

## Data Storage

The app stores user records in a file named `data.json` in the working directory.

Each record is saved as a JSON object representing a client or freelancer. This makes it easy to persist user information between sessions.

## Example Data Flow

```text
Client signs up
    -> creates project
    -> sends request to freelancer
    -> freelancer accepts
    -> project is assigned
    -> milestones are updated
    -> invoice is generated
    -> financial report is reviewed
```

## Summary

This application acts as a simplified freelance platform CLI where clients can post work, freelancers can register their skills, requests can be sent and reviewed, and milestone/invoice tracking can be handled inside a single terminal-based workflow.
