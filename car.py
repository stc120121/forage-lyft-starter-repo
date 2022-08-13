from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    @abstractmethod
    def needs_service(self):
        return self.engine.need_service() or self.battery.need_service() or self.tire.needs_service()
