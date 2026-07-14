from datetime import datetime, timedelta

from inventory_report.product import Product


def test_product_report() -> None:
    now = datetime.now()
    created = str(now - timedelta(days=365 * 2))
    expired = str(now + timedelta(days=365 * 40))
    serial_number = 'TY68 409C JJ43 ASD1 PL2F'
    name = 'skyline GTr 34'
    company = 'Nissan'
    _id = '1'
    storage_instructions = 'É uma relíquia, precisa ser conservada'
    product = Product(_id, name, company, created, expired,
                      serial_number, storage_instructions)

    expected = (
        f"The product {_id} - {name} "
        f"with serial number {serial_number} "
        f"manufactured on {created} "
        f"by the company {company} "
        f"valid until {expired} "
        "must be stored according to the following instructions: "
        f"{storage_instructions}."
    )

    assert expected == str(product)
