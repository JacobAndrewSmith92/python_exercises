import uuid

class LootBag():

    def list_child_toys(self, name):
        return ["ball"]

    def add_toy(self, toy, name):
        return "Toy added to bag"


    def add_toy(self, loot, kid):

        return f"{loot} {kid}"

    def set_child(self, kid):
        """Set childs takes a single argument that appends that item to children.txt

        Arguments:
            kid {[string]} -- [Kid name]
        """

        with open("data/children.txt", "a") as children:
            # id = uuid.uuid1()
            children.write(kid + "\n")
            # return kid


    def set_loot(self, loot):

        with open("data/loot.txt", "a") as allLoot:
            self.loot.write(loot + "\n")




# Creates list of Children:
# lootBag = LootBag()

# lootBag.set_child("John")
# lootBag.set_child("Josh")
# lootBag.set_child("Riley")
# lootBag.set_child("Jacob")
# lootBag.set_child("Megan")
# lootBag.set_child("Lexi")
# lootBag.set_child("Alex")

# lootBag.set_loot("piano")
# lootBag.set_loot("bike")
# lootBag.set_loot("book")
# lootBag.set_loot("wagon")

