from attacks.interface import AttackInterface
from utils.prompt import *
from model.loot import LootStore
import requests
from model.structure.loot import LootStructure
from model.history import HistoryStore
from model.structure.history import HistoryStructure
from utils.print import clear_line, space


class DirectoryBruteForce(AttackInterface):
    def __init__(self):
        super().__init__()
        self.loot_store = LootStore()
        self.history_store = HistoryStore()

    def title(self):
        return "Directory brute force"

    def prompt_for_params(self):
        self.url = prompt_param_required("URL with scheme (e.g. http://127.0.0.1:8080)")
        self.path_to_wordlist = prompt_param_with_default_value_and_name(
            "path to the wordlist",
            "resources/dir_bf/small.txt",
            "dirb's small.txt wordlist",
        )

    def run(self):
        wordlist = open(self.path_to_wordlist, "r")
        print("reading from wordlist file", self.path_to_wordlist)
        scan_id = self.history_store.store_one(
            HistoryStructure()
            .builder()
            .scan_type("dir_bf")
            .target_url(self.url)
            .build()
        )

        found_count = 0
        found_endpoints = []
        spacing = len(max(wordlist.readlines(), key=len))
        wordlist.seek(0)
        for endpoint in wordlist:
            endpoint = endpoint.rstrip("\n")
            full_url = self.url + "/" + endpoint
            print(f"trying {full_url}" + space(spacing), end="\r")

            r = requests.get(full_url)
            if r.status_code == 200:
                clear_line()
                print(f"found endpoint {endpoint}")
                self.loot_store.store_one(
                    LootStructure()
                    .builder()
                    .scan_id(scan_id)
                    .endpoint(endpoint)
                    .payload(endpoint)
                    .response_code(r.status_code)
                    .response_headers(str(r.headers))
                    .response_body(r.text)
                    .build()
                )
                found_count += 1
                found_endpoints.append("/" + endpoint)

        clear_line()
        print(f"found {found_count} endpoints")
        print(found_endpoints)
        input()
        wordlist.close()
