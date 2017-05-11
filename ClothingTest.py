import ClothingFunction
from ClothingFunction import Clothes
from ClothingFunction import Tees
from ClothingFunction import Polos
import unittest

class clothingTest(unittest.TestCase):


    def test_clothes_check_hoodie_instance_of_clothes(self):
        self.assertIsInstance(Tees(), Clothes)

    def test_clothes_check_when_number_sold_is_negative(self):
        self.assertEqual(Polos().sale(-4), "Invalid sale")

    def test_clothes_check_remaining_stock(self):
        result = Polos().sale(2)
        self.assertEqual(98, result)

    def test_clothes_check_if_number_sold_is_greater_than_stock(self):
        self.assertEqual(Polos().sale(105), "Sorry We don't have enough stock")


if __name__ == '__main__':
    unittest.main()