from datetime import datetime

from inventory_report.inventory import Inventory


class SimpleReport:
    def __init__(self) -> None:
        self._data = []

    def add_inventory(self, inventory: Inventory) -> None:
        self._data.append(inventory)

    def generate(self) -> str:
        oldest_manu_date = datetime.max
        companies_inventory: dict[str, int] = {}
        exp_dates: list[datetime] = []
        for inventory in self._data:
            for product in inventory.data:
                manu_date = datetime.strptime(
                    product.manufacturing_date, '%Y-%m-%d')
                expiration_date = datetime.strptime(
                    product.expiration_date, '%Y-%m-%d')
                exp_dates.append(expiration_date)
                if manu_date < oldest_manu_date:
                    oldest_manu_date = manu_date
                if product.company_name in companies_inventory:
                    companies_inventory[product.company_name] += 1
                else:
                    companies_inventory[product.company_name] = 1
        company_largest_inventory = max(
            companies_inventory.items(), key=lambda x: x[1])[0]
        now = datetime.now()
        future = [x for x in exp_dates if x >= now]
        closest_exp_date = min(future) if future else min(exp_dates)
        return (
            f"Oldest manufacturing date: {oldest_manu_date.date()}\n"
            f"Closest expiration date: {closest_exp_date.date()}\n"
            "Company with the largest "
            f"inventory: {company_largest_inventory}\n"
        )
