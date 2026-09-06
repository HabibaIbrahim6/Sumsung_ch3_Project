def get_new_milestone_status():
    status_options = {
        "1": "Pending",
        "2": "In Progress",
        "3": "Completed"
    }
    for key, value in status_options.items():
        print(f"{key}) {value}")

    choice = input("\nChoose new status: ")
    while choice not in status_options:
        choice = input("Invalid choice. Please try again: ")
    return status_options[choice]

def find_by_id(items, target_id):
    for item in items:
        if item.id == target_id:
            return item
    return None

def get_milestone_choice(minimum , maximum):
    while True:
        try:
            milestone_choice = int(
                input("Choose milestone to update: ")
            )
        except ValueError:
            print("Please enter a number.")
            continue

        if minimum <= milestone_choice <= maximum:
            return milestone_choice

        print("Invalid choice. Please try again.")

def get_menu_choice(minimum , maximum, message="Enter your choice "):
    while True:
        try:
            choice = int(
                input(message+f"({minimum}-{maximum}):")
            )
        except ValueError:
            print("Please enter a number")
            continue

        if minimum <= choice <= maximum:
            return choice

        print("Invalid choice, Try again")


def generate_id(prefix,counter):
    return f"{prefix}{counter:03}"


def get_milestones():
    print("Enter at least one milestone , enter 'EXIT' after finishing \n")
    milestones = []

    while True:
        milestone = input("Milestone: ").strip()

        if milestone == "":
            print("Please enter a milestone")
            continue

        if milestone.lower() == "exit":
            if len(milestones) == 0:
                print("Enter at least one milestone first.")
                continue
            else:
                break

        if milestone not in milestones:
            milestones.append(milestone)
        else:
            print("That milestone already exists. Try again.")

    return milestones


def create_list_of_candidate_projects_for_invoicing(current_client):
    return list(filter(lambda project: (project.status == "Completed" and project.invoice is None),current_client.projects_created))


#=================== CLOSURE FUNCTION ===================

def commission_rate(budget):
    if budget <= 500:
        rate = 0.05
    elif budget < 5000:
        rate = 0.08
    else:
        rate = 0.10

    def commission_amount():
        return budget * rate

    return commission_amount










#=================== FOR CLIENT MENU ===================



def print_client_menu():
    print("1. Create project")
    print("2. Assign project")
    print("3. Update milestone")
    print("4. Generate invoice")
    print("5. Log out")