from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, 'Margaret Hamiltons house', 'house',200)
    dao.insert(product)
    product_list = dao.select_all()
    names = [u.name for u in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'Bobs house', 'house',200)
    assigned_id = dao.insert(product)

    corrected_name = 'Bobs houses'
    product.id = assigned_id
    product.email = corrected_name

    dao.update(product)

    product_list = dao.select_all()
    names = [u.name for u in product_list]
    assert corrected_name in names

def test_product_delete():
    product = Product(None, 'Douglas house', 'house', 200)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)

    product_list = dao.select_all()
    names = [u.name for u in product_list]
    assert product.name not in names