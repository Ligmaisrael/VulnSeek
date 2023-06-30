import utils.menu as menu
import attacks.dir_bf as dir_bf

def main():
    dbf = dir_bf.DirectoryBruteForce()

    main_menu = menu.Menu([dbf])
    main_menu.run()
    
main()
