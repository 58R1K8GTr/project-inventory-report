from pathlib import Path
from typing import List

from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    """
    Process the report given a list of file paths and a report type,
    and returns the result.
    """
    if report_type.lower() not in ['simple', 'complete']:
        raise ValueError('Report type is invalid.')
    file_paths_filtered = [
        Path(x) for x in file_paths if Path(x).suffix in ('.json', '.csv')
    ]
    inventory = Inventory()
    for path in file_paths_filtered:
        if path.suffix == '.json':
            importer_json = JsonImporter(str(path))
            inventory.add_data(importer_json.import_data())
        else:
            importer_csv = CsvImporter(str(path))
            inventory.add_data(importer_csv.import_data())
    if report_type.lower() == 'simple':
        report = SimpleReport()
    else:
        report = CompleteReport()
    report.add_inventory(inventory)
    return report.generate()
