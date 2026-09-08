from .models.freelancemaneger import FreelanceManager
from .menus.main_menu import MainMenu


def main():

    manager = FreelanceManager()

    main_menu = MainMenu(manager)

    main_menu.show_menu()


if __name__ == "__main__":
    main()

