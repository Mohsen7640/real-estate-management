from abc import abstractmethod, ABC


class Estate(ABC):

    def __init__(self, reseller, area, rooms_count, built_year, region,
                 address, *args, **kwargs):
        self.reseller = reseller
        self.area = area
        self.rooms_count = rooms_count
        self.built_year = built_year
        self.region = region
        self.address = address

        super().__init__(*args, **kwargs)

    @abstractmethod
    def show_description(self):
        pass


class Apartment(Estate):

    def __init__(self, has_elevator, has_parking, floor, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor

        super().__init__(*args, **kwargs)

    def show_description(self):
        pass


class House(Estate):

    def __init__(self, has_yard, floors_count, *args, **kwargs):
        self.has_yard = has_yard
        self.floors_count = floors_count

        super().__init__(*args, **kwargs)

    def show_description(self):
        pass


class Store(Estate):

    def show_description(self):
        pass
