from attacks.interface import AttackInterface


class DirectoryBruteForce(AttackInterface):
    def title(self):
        return "Directory Brute Force"
    
    def run(self):
        print("pretending to try /admin")
        print("pretending to try /admin")
        print("pretending to try /admin")
        input()
        return
    
    def output_filename(self):
        return "example_filename-current_timestamp.txt"
