from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def drive(self, kilometers):
        if self.fuel - (self.fuel_consumption * kilometers) >= 0:
            self.fuel -= (self.fuel_consumption * kilometers)