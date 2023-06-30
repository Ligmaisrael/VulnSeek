import sys
from os import system
from attacks.interface import AttackInterface


class Menu:
    def __init__(self, attacks):
        """Every Attack must implement AttackInterface"""
        for atk in attacks:
            if not issubclass(type(atk), AttackInterface):
                raise TypeError(
                    f"all attacks must be a subclass of AttackInterface, {type(atk)} is not"
                )
        self.attacks = attacks

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
            elif choice > 0:
                choice -= 1
                self.attacks[choice].prompt_for_params()
                self.attacks[choice].run()
                choice = -1
        return

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

        if choice > len(self.attacks):
            clear_screen_with_message("Please choose one of the available options")
            return -1
        return choice

    def list_entries(self):
        for atk in self.attacks:
            print(f"{self.attacks.index(atk) + 1}. {atk.title()}")
        print("0. Quit")
        return

    def quit(self):
        print()
        print("Thank you for using VulnSeek")
        exit(0)
        return


print_without_newline = sys.stdout.write


def clear_screen():
    system("clear -x")


def clear_screen_with_message(message):
    clear_screen()
    print(message)
    print("Press enter to continue")
    input()
    clear_screen()
