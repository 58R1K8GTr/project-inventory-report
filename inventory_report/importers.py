from abc import ABC, abstractmethod
from json import load
from typing import Dict, Type

from .product import Product


class Importer(ABC):
    @abstractmethod
    def __init__(self, path: str) -> None:
        pass

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        self.path = path

    def import_data(self) -> list[Product]:
        with open(self.path, encoding='utf8') as file:
            json_file = [Product(**product) for product in load(file)]
        return json_file


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
