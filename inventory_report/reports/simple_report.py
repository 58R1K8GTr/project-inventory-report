from datetime import datetime

from inventory_report.inventory import Inventory


class SimpleReport:
    def __init__(self) -> None:
        self._data = []

    def add_inventory(self, inventory: Inventory) -> None:
        self._data.append(inventory)

    def generate(self) -> str:
        now = datetime.now()
        oldest_manu_date = now
        closest_exp_date = datetime(year=1700)
        companies_inventory = {}
        for inventory in self._data:
            for product in inventory.data():
                manu_date = datetime.strptime(
                    product.manufacturing_date, '%Y-%m-%d')
                expiration_date = datetime.strptime(
                    product.expiration_date, '%Y-%m-%d')
                if min([manu_date, oldest_manu_date]):
                    oldest_manu_date = manu_date
                if now > expiration_date > closest_exp_date:
                    closest_exp_date = expiration_date
                if product.company_name in companies_inventory:
                    companies_inventory[product.company_name] += 1
                else:
                    companies_inventory[product.company_name] = 1
        company_largest_inventory = max(
            companies_inventory.items(), key=lambda x: x[1])
        return (
            f"Oldest manufacturing date: {oldest_manu_date.date()}\n"
            f"Closest expiration date: {closest_exp_date.date()}\n"
            "Company with the largest"
            f"inventory: {company_largest_inventory}\n"
        )
