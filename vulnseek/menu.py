class Menu():

    def __init__(self, attacks):
        """Every Attack must implement AttackInterface"""
        self.attacks = attacks
    
    def run(self):
        choice = -1;
        while (choice != 0):
            self.list_entries()
            choice = self.prompt()

            if choice == 0:
                self.quit()
            elif choice > 0:
                choice -= 1
                self.attacks[choice].run()
                choice = -1
        return

    def prompt(self):
        try:
            choice = int(input())
        except ValueError:
            print("input a number")
            return -1
        except KeyboardInterrupt:
            self.quit()

        if choice > len(self.attacks):
            print("choose one of the options")
            return -1
        return choice
    
    def list_entries(self):
        for atk in self.attacks:
            print(self.attacks.index(atk)+1, atk.title())
        return

    def quit(self):
        print()
        print("Thank you for using VulnSeek")
        exit(0)
        return
