import unittest
from task4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    
    def setUp(self):
        self.cart = ShoppingCart()
    
    def test_add_single_item(self):
        self.cart.add_item("Apple", 1.00)
        self.assertEqual(self.cart.total_cost(), 1.00)
    
    def test_add_multiple_items(self):
        self.cart.add_item("Apple", 1.00)
        self.cart.add_item("Banana", 0.50)
        self.assertEqual(self.cart.total_cost(), 1.50)
    
    def test_add_duplicate_item(self):
        self.cart.add_item("Apple", 1.00)
        self.cart.add_item("Apple", 0.50)
        self.assertEqual(self.cart.total_cost(), 1.50)
    
    def test_remove_existing_item(self):
        self.cart.add_item("Apple", 1.00)
        self.cart.add_item("Banana", 0.50)
        self.cart.remove_item("Apple")
        self.assertEqual(self.cart.total_cost(), 0.50)
    
    def test_remove_nonexistent_item(self):
        result = self.cart.remove_item("Orange")
        self.assertEqual(result, "Item not found in cart.")
    
    def test_total_cost_empty_cart(self):
        self.assertEqual(self.cart.total_cost(), 0)
    
    def test_remove_all_items(self):
        self.cart.add_item("Apple", 1.00)
        self.cart.add_item("Banana", 0.50)
        self.cart.remove_item("Apple")
        self.cart.remove_item("Banana")
        self.assertEqual(self.cart.total_cost(), 0)


if __name__ == '__main__':
    unittest.main()