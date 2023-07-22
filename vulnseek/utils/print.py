from os import system


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


def quit_with_msg():
    print()
    print("Thank you for using VulnSeek")
    exit(0)
