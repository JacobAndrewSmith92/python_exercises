import sys
import unittest
from lootbag import LootBag


# Items can be added to bag, and assigned to a child.
# Items can be removed from bag, per child. Removing ball from the bag should not be allowed. A child's name must be specified.
# Must be able to list all children who are getting a toy.
# Must be able to list all toys for a given child's name.
# Must be able to set the delivered property of a child, which defaults to false to true.


class TestLootBag(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bag = LootBag()


    def test_can_list_toys_from_bag_for_child(self):
        toy = "ball"
        mikey_toys = self.bag.list_child_toys("Mikey")
        self.assertIn(toy, mikey_toys)

    def test_setting_child(self):
        lootin = LootBag()

        with open("data/children.txt", "r") as children:
            self.assertFalse("Megan" in children.read())
            lootin.set_child("Megan")
            self.assertTrue("Megan" in children.read())

    def test_add_toy_to_bag(self):
        bag = LootBag()
        toy = "ball"
        self.assertEqual(bag.add_toy("ball", "Mikey"), "Toy added to bag")

        # toy = "truck"
        # toy_list = self.bag.list_child_toys("Mikey")
        # self.assertNotIn(toy, toy_list)
        # self.bag.add_toy("truck", "Mikey")
        # self.bag.list_child_toys("Mikey")
        # self.assertIn(toy, toy_list)



if __name__ == '__main__':
    unittest.main()