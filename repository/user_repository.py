import models
from models.enum_types import UserType
from models.user import User
import sqlite3
db = sqlite3.connect('estore.db')
try:
    cur = db.cursor()
    cur.execute('''CREATE TABLE User(user_id INTEGER PRIMARY KEY AUTO INCREAMENT,
     first_name TEXT(20) NOT NULL, last_name TEXT(20) NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL,
      card_id INTEGER);''')
    print('Table created successfully')
except:
    print('error in operation')
    db.rollback()
db.close()

Address = 'CREATE TABLE Address(address_id INTEGER PRIMARY KEY AUTO INCREAMENT, street_number Text not null, street_name text not null,' \
          'city text, state text(20) not null)'

Category = 'CREATE TABLE Category(category_id INTEGER PRIMARY KEY AUTO INCREAMENT, name TEXT not null, description text)'

Product = 'CREATE TABLE Product(product_id INTEGER PRIMARY KEY AUTO INCREAMENT, product_name text, description text,' \
          'discount float, category_id INTEGER FOREIGN KEY references Category(category_id) on delete cascade)'

Cart = 'CREATE TABLE Cart(cart_id INTEGER PRIMARY KEY AUTO INCREAMENT, product_id INTEGER FOREIGN KEY references Product(product_id))'

Shop = 'CREATE TABLE Shop(shop_id INTEGER PRIMARY KEY autoincreament, name text not null, description text,' \
       ' merchant_id INTEGER  foreign key  references Merchant(merchant-id), product_id INTEGER foreign key references Product(product_id))'

Merchant = 'CREATE TABLE Merchant(merchant_id INTEGER PRIMARY KEY AUTO INCREMENT,' \
           'address_id INTEGER references Address(address_id), card_id INTEGER references CardDetails(card_id),' \
           ' user_id INTEGER foreign key references User(user_id) on delete  cascade, shop_id INTEGER foreign key references Shop(shop_id))'

customer = 'CREATE TABLE Customer(customer_id INTEGER PRIMARY KEY AUTO INCREMENT,' \
           'address_id INTEGER references Address(address_id), card_id INTEGER references CardDetails(card_id),' \
           ' user_id INTEGER foreign key references User(user_id) on delete  cascade )'

class UserRepository:

    # @staticmethod
    def __init__(self):
        self.users = {"customer": [],
                      "Merchant": []
                      }







