# Permission options: r: read only, w: write only, a: appending, r+: read and write

# 1. Create a single class that implements all functionality.
# 2. Create a method for reading the car makes file.
# 3. Create a method for reading the car models file.

# 4. Create a method that invokes the previous two methods and generates a dictionary.
# 5. The dictionary keys will be the make names.
# 6. The value for each key will be a list of model names.

# Ex.

# {
#     "Toyota": ["Camry"],
#     ...
# }



class CarList():

    def __init__(self):
        self.makes = list()
        self.models = list()

    def _read_car_make(self):
        with open("car_makes.txt", "r") as makes:
            car_makes = makes.readlines()
            self.makes = [make.split('\n', 1)[0] for make in car_makes]

    def _read_car_models(self):
        with open("car_models.txt", "r") as models:
            car_models = models.readlines()
            split_equal_models = [model.split('=', 1)[1] for model in car_models]
            self.models = [model.split('\n', 1)[0] for model in split_equal_models]

    def create_car_dict(self):
        self._read_car_make()
        self._read_car_models()
        cars = dict(zip(self.makes, self.models))
        return cars

    # def __str__(self):
    #         return [f"My list of models {make}" for make in self.makes]

car = CarList()
print(car.create_car_dict())