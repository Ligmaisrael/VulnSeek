from attacks.interface import AttackInterface
from utils.print import *
from utils.prompt import validate_number_selection
from utils.scan_detail import ScanDetail
from utils.scan_history import ScanHistory


class Menu:
    def __init__(self, attacks):
        """Every Attack must implement AttackInterface"""
        for atk in attacks:
            if not issubclass(type(atk), AttackInterface):
                raise TypeError(
                    f"all attacks must be a subclass of AttackInterface, {type(atk)} is not"
                )
        self.attacks = attacks
        self.scan_history = ScanHistory()

    def run(self):
        while True:
            self.show_menu()
            choice = validate_number_selection(len(self.attacks) + 2)

            if choice == 0:
                quit_with_msg()
            elif choice == len(self.attacks) + 1:
                last_scan = self.scan_history.get_last()
                last_scan_detail = ScanDetail(last_scan)
                last_scan_detail.view()
            elif choice == len(self.attacks) + 2:
                self.scan_history.view_history()
            else:
                self.attacks[choice - 1].run()

    def show_menu(self):
        clear_screen()
        print("Welcome to VulnSeek")
        print()
        for atk in self.attacks:
            print(f"{self.attacks.index(atk) + 1}. {atk.title()}")
        print(f"{len(self.attacks)+1}. View last scan result")
        print(f"{len(self.attacks)+2}. View scan history")
        print("0. Quit")
        print("Please choose one of the above options")
