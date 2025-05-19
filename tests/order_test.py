import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all.clear()
        self.customer = Customer("Eli")
        self.coffee = Coffee("Cappuccino")

    def test_valid_order(self):
        order = Order(self.customer, self.coffee, 6.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 6.5)

    def test_invalid_customer_type(self):
        with self.assertRaises(TypeError):
            Order("NotACustomer", self.coffee, 5.0)

    def test_invalid_coffee_type(self):
        with self.assertRaises(TypeError):
            Order(self.customer, "NotACoffee", 5.0)

    def test_invalid_price_type(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "5.0")

    def test_invalid_price_range(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)

    def test_order_immutable_properties(self):
        order = Order(self.customer, self.coffee, 4.0)
        with self.assertRaises(AttributeError):
            order.price = 8.0
        with self.assertRaises(AttributeError):
            order.customer = Customer("New")
        with self.assertRaises(AttributeError):
            order.coffee = Coffee("NewCoffee")
