from abc import ABC

from car import Car
from engine.Engine import Engine


class SternmanEngine(Engine):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def need_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
