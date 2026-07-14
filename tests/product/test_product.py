from datetime import datetime, timedelta

from inventory_report.product import Product


def test_create_product() -> None:
    now = datetime.now()
    expired = now + timedelta(days=1)
    created = now - timedelta(days=5)
    product = Product(
        '1', 'skyline GTr 34', 'Nissan', str(created), str(expired), '123',
        'instruções de armazenamento.'
    )
    assert product.id == '1'
    assert product.company_name == 'Nissan'
    assert product.product_name == 'skyline GTr 34'
    assert product.manufacturing_date == str(created)
    assert product.expiration_date == str(expired)
    assert product.serial_number == '123'
    assert product.storage_instructions == 'instruções de armazenamento.'
