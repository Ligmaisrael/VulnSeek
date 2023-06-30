from attacks.interface import AttackInterface
from utils.prompt import *
import requests

class DirectoryBruteForce(AttackInterface):
    def title(self):
        return "Directory Brute Force"
    
    def prompt_for_params(self):
        self.url = prompt_param_required("URL with scheme (e.g. http://127.0.0.1:8080)")
        self.path_to_wordlist = prompt_param_with_default_value_and_name(
            "path to the wordlist",
            "resources/dir_bf/small.txt",
            "dirb's small.txt wordlist")
        return
    
    def run(self):
        wordlist = open(self.path_to_wordlist, "r")
        print("reading from wordlist file", self.path_to_wordlist)

        found_count = 0
        found_endpoints = []
        for endpoint in wordlist:
            endpoint = endpoint.rstrip("\n")
            full_url = self.url + "/" + endpoint
            print(f"trying {full_url}")

            r = requests.get(full_url)
            if r.status_code == 200:
                print(f"found endpoint {endpoint}")
                found_count += 1
                found_endpoints.append("/"+endpoint)

        print(f"found {found_count} endpoints")
        print(found_endpoints)
        input()
        wordlist.close()
        return
    
    def output_filename(self):
        return "example_filename-current_timestamp.txt"
