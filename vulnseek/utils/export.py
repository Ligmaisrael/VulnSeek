import os
from io import TextIOWrapper

from model.history import HistoryStore
from model.loot import LootStore
from model.structure.history import HistoryStructure
from model.structure.loot import LootStructure
from utils.prompt import prompt_param_required


def export_to_md_file(scan_id) -> bool:
    while True:
        filename = (
            prompt_param_required("desired filename without extension (.md)") + ".md"
        )
        if os.path.isfile(filename):
            print(f'File "{filename}" exists, please input a different name')
            continue
        else:
            print(f'Saving to "{filename}"')
            break
    output_file = open(filename, "w")

    scan = _export_scan_history(output_file, scan_id)
    _export_scan_loots(output_file, scan)

    output_file.close()
    print(f'Successfully saved to "{filename}"')
    print("Now returning you back")
    input()
    return True


def _export_scan_history(output_file: TextIOWrapper, scan_id: int) -> HistoryStructure:
    history_store = HistoryStore()
    scan_from_db = history_store.get_by_scan_id(scan_id)
    scan = HistoryStructure.from_row(scan_from_db)
    output_file.write(scan.export_as_md())
    return scan


def _export_scan_loots(output_file: TextIOWrapper, scan: HistoryStructure):
    loot_store = LootStore()
    loots_from_db = loot_store.get_by_scan_id(scan.scan_id)
    output_file.write("## Successful Payloads\n\n")
    if len(loots_from_db) == 0:
        output_file.write("No payloads were successful in this attack\n")
    else:
        for loot_from_db in loots_from_db:
            loot = LootStructure.from_row(loot_from_db)
            output_file.write(loot.export_as_md())
