from battery.battery import Battery


class Nubbin(Battery):

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_data = current_date

    def needs_service(self):
        return self.last_service_data.year+4<self.current_date.year
