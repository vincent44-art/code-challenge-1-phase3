import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer







import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order.all.clear()  # Reset global state before each test
        self.customer = Customer("Alice")
        self.coffee1 = Coffee("Latte")
        self.coffee2 = Coffee("Mocha")

    def test_valid_name(self):
        self.assertEqual(self.customer.name, "Alice")

    def test_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Customer(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("x" * 16)

    def test_name_setter(self):
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")

    def test_orders_and_coffees(self):
        o1 = Order(self.customer, self.coffee1, 5.0)
        o2 = Order(self.customer, self.coffee2, 6.0)
        o3 = Order(self.customer, self.coffee1, 7.0)

        self.assertEqual(len(self.customer.orders()), 3)
        self.assertIn(self.coffee1, self.customer.coffees())
        self.assertIn(self.coffee2, self.customer.coffees())
        self.assertEqual(len(self.customer.coffees()), 2)

    def test_create_order(self):
        order = self.customer.create_order(self.coffee1, 4.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee1)
        self.assertEqual(order.price, 4.5)

    def test_most_aficionado(self):
        c2 = Customer("Ben")
        c2.create_order(self.coffee1, 3.0)
        self.customer.create_order(self.coffee1, 5.0)
        self.customer.create_order(self.coffee1, 5.0)

        result = Customer.most_aficionado(self.coffee1)
        self.assertEqual(result.name, "Alice")

    def test_most_aficionado_no_orders(self):
        result = Customer.most_aficionado(self.coffee1)
        self.assertIsNone(result)

