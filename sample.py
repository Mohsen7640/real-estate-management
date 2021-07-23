from random import choice

from models import (Reseller, Region, ApartmentSell, ApartmentRent, HouseSell,
                    HouseRent, StoreSell, StoreRent)

FIRSTNAME = ['Sherry', 'Stephen', 'William', 'Joshua']
LASTNAME = ['Duncan', 'Tolson', 'McNew', 'Caraway']
MOBILE = ['09121231234', '09124564567', '09121211122', '09121459956']


def create_samples():
    # Create Reseller
    for mobile in MOBILE:
        Reseller(
            first_name=choice(FIRSTNAME),
            last_name=choice(LASTNAME),
            phone_number=mobile
        )

    # Create Region
    region_1 = Region(name='Region#1')
    region_2 = Region(name='Region#2')

    # Create Advertisement
    ApartmentSell(
        reseller=Reseller.object_lists[0], area=80, rooms_count=2,
        built_year=1392, region=region_1, address='Sample text...',
        has_elevator=True, has_parking=True, floor=2,
        price_per_meter=10, discountable=True, convertable=False
    )

    ApartmentSell(
        reseller=Reseller.object_lists[3], area=120, rooms_count=2,
        built_year=1394, region=region_2, address='Sample text...',
        has_elevator=True, has_parking=True, floor=2,
        price_per_meter=12, discountable=True, convertable=False
    )

    ApartmentRent(
        reseller=Reseller.object_lists[0], area=80, rooms_count=2,
        built_year=1393, region=region_1, address='Sample text...',
        has_elevator=True, has_parking=True, floor=2,
        initial_price=30, monthly_price=2,
        discountable=True, convertable=False
    )

    print('#' * 30, '\t Create Samples \t', '#' * 30)
