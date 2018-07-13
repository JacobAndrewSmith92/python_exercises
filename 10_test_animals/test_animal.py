import unittest
import sys
sys.path.append('../')
from animal import Animal
from animal import Dog


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")
        self.jonnie = Animal("Jonnie")

    def test_animal_creation(self):

        joe = Dog("Joe")

        self.assertIsInstance(joe, Dog)
        self.assertIsInstance(joe, Animal)
        self.assertIsInstance(self.jonnie, Animal)

    def test_animal_can_set_legs(self):

        murph = Dog("murph")
        murph.set_legs(6)
        self.assertEqual(murph.legs, 6)

    def test_animal_can_set_species(self):

        self.bob.set_species("Labrador")
        self.assertIs(self.bob.species, "Labrador")

    def test_animal_can_get_species(self):

        self.assertIs(self.bob.get_species(), "Dog")

    def test_animal_can_walk(self):

        self.bob.set_legs(6)
        self.bob.walk()
        self.assertEqual(self.bob.speed, 1.2)

    def test_animal_name(self):

        self.assertEqual(self.bob.name, "Bob")




if __name__ == '__main__':
    unittest.main()