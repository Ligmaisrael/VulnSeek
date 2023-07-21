from attacks.interface import AttackInterface
from utils.print import *
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
        choice = -1
        while choice != 0:
            clear_screen()
            print("Welcome to VulnSeek")
            print()
            self.list_entries()
            choice = self.prompt()

            if choice == 0:
                self.quit()
            elif choice > 0 and choice <= len(self.attacks):
                choice -= 1
                self.attacks[choice].prompt_for_params()
                self.attacks[choice].run()
                choice = -1
            elif choice == len(self.attacks) + 1:
                last_scan = self.scan_history.get_last()
                scan_detail = ScanDetail(last_scan)
                scan_detail.view()
            elif choice == len(self.attacks) + 2:
                self.scan_history.view_history()

    def prompt(self):
        print("Please choose one of the above options")
        print_without_newline("> ")
        choice = -1
        try:
            choice = int(input())
        except ValueError:
            clear_screen_with_message("Please input a number")
            return -1
        except KeyboardInterrupt:
            self.quit()

        if choice > len(self.attacks) + 2:
            clear_screen_with_message("Please choose one of the available options")
            return -1
        return choice

    def list_entries(self):
        for atk in self.attacks:
            print(f"{self.attacks.index(atk) + 1}. {atk.title()}")
        print(f"{len(self.attacks)+1}. View last scan result")
        print(f"{len(self.attacks)+2}. View scan history")
        print("0. Quit")

    def quit(self):
        print()
        print("Thank you for using VulnSeek")
        exit(0)
