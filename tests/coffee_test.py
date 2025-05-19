import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order.all.clear()
        self.coffee = Coffee("Espresso")
        self.c1 = Customer("Ava")
        self.c2 = Customer("Liam")

    def test_valid_name(self):
        self.assertEqual(self.coffee.name, "Espresso")

    def test_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Coffee(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Coffee("Ab")

    def test_name_immutable(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Americano"

    def test_orders_and_customers(self):
        self.c1.create_order(self.coffee, 4.0)
        self.c2.create_order(self.coffee, 5.0)
        self.assertEqual(len(self.coffee.orders()), 2)
        self.assertIn(self.c1, self.coffee.customers())
        self.assertIn(self.c2, self.coffee.customers())

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 0)
        self.c1.create_order(self.coffee, 3.0)
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 0)
        self.c1.create_order(self.coffee, 3.0)
        self.c2.create_order(self.coffee, 5.0)
        self.assertEqual(self.coffee.average_price(), 4.0)
