from attacks.interface import AttackInterface
from utils.prompt import *

class DirectoryBruteForce(AttackInterface):
    def title(self):
        return "Directory Brute Force"
    
    def prompt_for_params(self):
        self.url = prompt_param_required("URL")
        self.path_to_wordlist = prompt_param_with_default_value_and_name(
            "path to the wordlist",
            "resources/dir_bf/small.txt",
            "dirb's small.txt wordlist")
        return
    
    def run(self):
        wordlist = open(self.path_to_wordlist, "r")
        print("reading from wordlist file", self.path_to_wordlist)

        for line in wordlist:
            print("trying", self.url + "/" + line.rstrip("\n"))

        input()
        wordlist.close()
        return
    
    def output_filename(self):
        return "example_filename-current_timestamp.txt"
