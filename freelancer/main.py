from .models.freelancemaneger import FreelanceManager
from .menus.main_menu import MainMenu


def main():

    # Create the main system manager
    manager = FreelanceManager()

    # Create the main menu and pass the manager to it
    main_menu = MainMenu(manager)

    # Start the application
    main_menu.show_menu()


if __name__ == "__main__":
    main()

