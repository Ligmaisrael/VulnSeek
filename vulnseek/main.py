import utils.menu as menu
from attacks.dir_bf.dir_bf import DirectoryBruteForce


def main():
    dbf = DirectoryBruteForce()

    main_menu = menu.Menu([dbf])
    main_menu.run()


main()
