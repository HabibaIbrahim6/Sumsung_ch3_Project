import os
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

if __package__ in (None, ""):
    sys.path.insert(0, str(PROJECT_ROOT))

from freelancer.models.freelancemaneger import FreelanceManager
from freelancer.menus.main_menu import MainMenu


def main():
    os.chdir(PROJECT_ROOT)
    manager = FreelanceManager()

    main_menu = MainMenu(manager)

    main_menu.show_menu()


if __name__ == "__main__":
    main()

