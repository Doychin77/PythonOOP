from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def drive(self, kilometers):
        if self.fuel - (self.fuel_consumption * kilometers) >= 0:
            self.fuel -= (self.fuel_consumption * kilometers)



