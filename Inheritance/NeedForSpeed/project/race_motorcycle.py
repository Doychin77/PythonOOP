from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def drive(self, kilometers):
        if self.fuel - (self.fuel_consumption * kilometers) >= 0:
            self.fuel -= (self.fuel_consumption * kilometers)