from models.enum_types import UserType
from repository.user_repository import UserRepository

users = UserRepository()


def add_user(user):
    if user.type_of_user is UserType.CUSTOMER:
        users.users["customer"].append(user)
    elif user.type_of_user is UserType.MERCHANT:
        users.users["Merchant"].append(user)


def find_all_customers():
    return users.users["customer"]

# def


def find_all_merchants():
    return users.users["Merchant"]


def find_customer_by_id(id):
    for customer in users.users['customer']:
        if customer.id == id:
            return customer


def find_merchant_by_id(id):
    for merchant in users.users['Merchant']:
        if merchant.id == id:
            return merchant
