from tire.tire import Tire


class Octoprime(Tire):

    def __init__(self, wear_sensor):
        self.sensor = wear_sensor

    def needs_service(self):
        return self.sensor.sum() >= 3