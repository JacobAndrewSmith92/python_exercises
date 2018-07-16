import sys
import unittest
from lootbag import LootBag


class testLootBag(unittest.TestCase):




    def test_adding_loot_kid(self):

        suzy = LootBag()

        self.assertEqual(suzy.add_toy("Suzy", "bike"), "bike Suzy")
        # self.assertEqual(suzy.add("Suzy", "doll"), "Suzzy doll") Returns False

    def test_setting_child(self):

        lootin = LootBag()

        with open("data/children.txt", "r") as children:
            self.assertFalse("Riley" in children.read())
            lootin.set_child("Riley")
            self.assertTrue("Riley" in children.read())



if __name__ == '__main__':
    unittest.main()