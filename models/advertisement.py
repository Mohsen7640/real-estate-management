from abc import ABC, abstractmethod

from models.estate import Apartment, House, Store
from models.deal import Sell, Rent
from models.base import Base


class Advertisement(ABC):

    @abstractmethod
    def show_detail(self):
        pass


class ApartmentSell(Advertisement, Apartment, Sell, Base):

    def show_detail(self):
        pass


class ApartmentRent(Advertisement, Apartment, Rent, Base):

    def show_detail(self):
        pass


class HouseSell(Advertisement, House, Sell, Base):

    def show_detail(self):
        pass


class HouseRent(Advertisement, House, Rent, Base):

    def show_detail(self):
        pass


class StoreSell(Advertisement, Store, Sell, Base):

    def show_detail(self):
        pass


class StoreRent(Advertisement, Store, Rent, Base):

    def show_detail(self):
        pass
