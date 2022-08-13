from battery.nubbin import Nubbin
from battery.spindler import Spindler
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.tire import Tire


class CarFactory:
    def create_calliope(self,current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensor):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = Spindler(last_service_date, current_date)
        tire = Tire(tire_wear_sensor)
        return Car(engine, battery, tire)

    def create_glissade(self,current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensor):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = Spindler(last_service_date, current_date)
        tire = Tire(tire_wear_sensor)
        return Car(engine, battery)

    def create_palindrome(self,current_date, last_service_date, warning_light_on, tire_wear_sensor):
        engine = SternmanEngine(last_service_date, warning_light_on)
        battery = Spindler(last_service_date, current_date)
        tire = Tire(tire_wear_sensor)
        return Car(engine, battery, tire)

    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensor):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        tire = Tire(tire_wear_sensor)
        return Car(engine, battery, tire)

    def create_thovex(self,current_date, last_service_date, current_mileage, last_service_mileage, tire_wear_sensor):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        tire = Tire(tire_wear_sensor)
        return Car(engine, battery, tire)

