import unittest

import models
import service.user_service
from exception.exception import CardDoesNotExistException, InvalidAddressException, CategoryNotFoundException
from models.enum_types import UserType, CardType
from models.user import User, Address, CardDetails, Customer, Shop, Category, Product, Merchant
from repository.user_repository import UserRepository
from service import user_service


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_that_user_has_first_name(self):
        user = User(id='', first_name='Ifeanyi', last_name='Osuji', email='oi@gmail.com', password='2217',
                    type_of_user=UserType.ADMIN)
        self.assertEqual('Ifeanyi', user.first_name)

    def test_that_user_has_last_name(self):
        user = User(id='', first_name='Ifeanyi', last_name='Osuji', email='oi@gmail.com', password='2217',
                    type_of_user=UserType.ADMIN)
        self.assertEqual('Osuji', user.last_name)

    def test_that_user_has_email(self):
        user = User(id='', first_name='Ifeanyi', last_name='Osuji', email='oi@gmail.com', password='2217',
                    type_of_user=UserType.CUSTOMER)
        self.assertEqual('oi@gmail.com', user.email)

    def test_that_user_has_password(self):
        user = User(id='', first_name='Ifeanyi', last_name='Osuji', email='oi@gmail.com', password='2217',
                    type_of_user=UserType.ADMIN)
        self.assertEqual('2217', user.password)

    def test_that_individual_is_a_user(self):
        user = User(id='', first_name='Ifeanyi', last_name='Osuji', email='oi@gmail.com', password='2217',
                    type_of_user=UserType.CUSTOMER)
        self.assertEqual(UserType.CUSTOMER, user.type_of_user)

    def test_that_individual_must_be_of_type_user(self):
        user = User(id='', first_name='Ifeanyi', last_name='Osuji', email='oi@gmail.com', password='2217',
                    type_of_user=UserType.ADMIN)
        self.assertEqual(UserType.ADMIN, user.type_of_user)

    def test_that_user_address_has_number(self):
        address = Address(1233)
        self.assertEqual(1233, address.number)

    def test_that_user_address_has_street_number(self):
        address = Address(1233, 'Sabo')
        self.assertEqual('Sabo', address.street_name)

    def test_that_user_address_has_town(self):
        address = Address(1233, 'Sabo', 'Yaba')
        self.assertEqual('Yaba', address.town)

    def test_that_user_address_has_state(self):
        address = Address(1233, 'Sabo', 'Yaba', 'Lagos')
        self.assertEqual('Lagos', address.state)

    def test_that_user_card_has_name(self):
        card = CardDetails('Ifeanyi Osuji', CardType.VISA)
        self.assertEqual('Ifeanyi Osuji', card.name)

    def test_that_user_card_has_type(self):
        card = CardDetails('Ifeanyi Osuji', CardType.VISA)
        self.assertEqual(CardType.VISA, card.card_type)

    def test_that_user_card_has_number(self):
        card = CardDetails('Ifeanyi Osuji', CardType.VISA, card_number='123456123')
        self.assertEqual('123456123', card.card_number)

    def test_that_user_card_has_pin(self):
        card = CardDetails('Ifeanyi Osuji', CardType.VISA, '123456123', 1234)
        self.assertEqual(1234, card.pin)

    def test_that_customer_card_is_of_card_type(self):
        self.assertRaises(CardDoesNotExistException, CardDetails, 'VISA')

    def test_that_customer_address_is_of_type_address(self):
        address = Address()
        card = CardDetails(card_type=CardType.VISA)
        customer = Customer(type_of_user=UserType.CUSTOMER, address=address, card_details=card)
        self.assertEqual(address, customer.address)

    def test_that_category_has_name(self):
        category = Category(name='groceries')
        self.assertEqual('groceries', category.name)

    def test_that_category_has_description(self):
        category = Category(description='Food items')
        self.assertEqual('Food items', category.description)

    def test_that_product_has_id(self):
        product = Product(id='001', category=Category())
        self.assertEqual('001', product.id)

    def test_that_product_has_name(self):
        product = Product(name='iPhone 19', category=Category())
        self.assertEqual('iPhone 19', product.name)

    def test_that_product_has_description(self):
        product = Product(description="1 terabite, 18git ram, 24 megapixel", category=Category())
        self.assertEqual('1 terabite, 18git ram, 24 megapixel', product.description)

    def test_that_product_has_price(self):
        product = Product(price=900000.00, category=Category())
        self.assertEqual(900000.00, product.price)

    def test_that_product_has_category(self):
        category = Category()
        product = Product(category=category)
        self.assertEqual(category, product.category)

    def test_that_product_category_cannot_be_of_another_type(self):
        self.assertRaises(CategoryNotFoundException, Product, category='Groceries')

    def test_that_shop_has_id(self):
        shop = Shop(id=12)
        self.assertEqual(12, shop.id)

    def test_that_shop_has_name(self):
        shop = Shop(name='Aboki')
        self.assertEqual('Aboki', shop.name)

    def test_shop_description(self):
        shop = Shop(description='maggie shop that has every thing you need')
        self.assertEqual('maggie shop that has every thing you need', shop.description)

    def test_that_user_repository_has_users(self):
        address = Address()
        card = CardDetails(card_type=CardType.VISA)
        customers = Customer(type_of_user=UserType.CUSTOMER, address=address, card_details=card)
        user_repository = UserRepository()
        user_service.add_user(user=customers)
        self.assertEqual(1, len(user_service.users.users["customer"]))
        merchant = Merchant(first_name='Janet', last_name='Akin', type_of_user=UserType.MERCHANT, address=address,
                            card_details=CardDetails(card_type=CardType.VISA))
        user_service.add_user(merchant)
        self.assertEqual(1, len(user_service.users.users["Merchant"]))

    def test_that_all_customers_can_be_found(self):
        customer1 = Customer(first_name='Kelvin', last_name="Okoro", type_of_user=UserType.CUSTOMER, address=Address(),
                             card_details=CardDetails(card_type=CardType.VISA))
        customer2 = Customer(first_name="Confi", last_name="Okere", type_of_user=UserType.CUSTOMER, address=Address(),
                             card_details=CardDetails(card_type=CardType.VERVE))
        customer3 = Customer(first_name="Janet", last_name="Ishola", type_of_user=UserType.CUSTOMER, address=Address(),
                             card_details=CardDetails(card_type=CardType.MASTERCARD))
        user_service.add_user(user=customer1)
        user_service.add_user(user=customer2)
        user_service.add_user(user=customer3)
        self.assertEqual(3, len(user_service.users.users['customer']))

    def test_that_customer_can_be_found_by_id(self):
        customer1 = Customer(id=1,first_name='Kelvin', last_name="Okoro", type_of_user=UserType.CUSTOMER, address=Address(),
                             card_details=CardDetails(card_type=CardType.VISA))
        customer2 = Customer(id=2, first_name="Confi", last_name="Okere", type_of_user=UserType.CUSTOMER, address=Address(),
                             card_details=CardDetails(card_type=CardType.VERVE))
        customer3 = Customer(id=3, first_name="Janet", last_name="Ishola", type_of_user=UserType.CUSTOMER, address=Address(),
                             card_details=CardDetails(card_type=CardType.MASTERCARD))
        user_service.add_user(user=customer1)
        user_service.add_user(user=customer2)
        user_service.add_user(user=customer3)
        self.assertEqual(customer3, user_service.find_customer_by_id(3))

    def test_that_merchant_can_be_found_by_id(self):
        merchant1 = Merchant(id=1,first_name='Kelvin', last_name="Okoro", type_of_user=UserType.MERCHANT, address=Address(),
                             card_details=CardDetails(card_type=CardType.VISA))
        merchant2 = Merchant(id=2, first_name="Confi", last_name="Okere", type_of_user=UserType.MERCHANT, address=Address(),
                             card_details=CardDetails(card_type=CardType.VERVE))
        merchant3 = Merchant(id=3, first_name="Janet", last_name="Ishola", type_of_user=UserType.MERCHANT, address=Address(),
                             card_details=CardDetails(card_type=CardType.MASTERCARD))
        user_service.add_user(user=merchant1)
        user_service.add_user(user=merchant2)
        user_service.add_user(user=merchant3)
        self.assertEqual(merchant3, user_service.find_merchant_by_id(3))


if __name__ == '__main__':
    unittest.main()
