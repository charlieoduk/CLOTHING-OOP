import ClothingFunctions
import unittest

class clothingTest(unittest.TestCase):

    def setUp(self):
        self.clothing = ClothingFunctions.Clothes()

    def test_clothes_check_hoodie_instance_of_clothes(self):
        self.assertTrue(issubclass(self.clothing.Tees, self.clothing))

    def test_clothes_check_when_number_sold_is_negative(self):
        self.assertEqual(self.clothing.Polos(-4), "Invalid sale")

    def test_clothes_check_remaining_stock(self):
        result = self.clothing.Polos(2)
        self.assertEqual(98, result)

    def test_clothes_check_if_number_sold_is_greater_than_stock(self):
        self.assertEqual(self.clothing.Polos(105), "Sorry We don't have enough stock")


if __name__ == '__main__':
    unittest.main()