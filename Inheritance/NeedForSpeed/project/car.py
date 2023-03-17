from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def drive(self, kilometers):
        if self.fuel - (self.fuel_consumption * kilometers) >= 0:
            self.fuel -= (self.fuel_consumption * kilometers)