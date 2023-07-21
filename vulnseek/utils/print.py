from os import system
import sys


print_without_newline = sys.stdout.write


def clear_screen():
    system("clear -x")


def clear_screen_with_message(message):
    clear_screen()
    print(message)
    print("Press enter to continue")
    input()
    clear_screen()


def clear_line():
    print(end="\x1b[2K")


def space(n):
    return " " * n
