from sample import create_samples
from models import (ApartmentSell, ApartmentRent, HouseSell, HouseRent,
                    StoreSell, StoreRent)


class Handler:
    ADVERTISEMENTS = [ApartmentSell, ApartmentRent, HouseSell, HouseRent,
                      StoreSell, StoreRent]
    SWITCHES = {
        'r': 'get_reports',
        't': 'get_tickets'
    }

    @staticmethod
    def get_reports():
        print('#' * 30, '\t Reports \t', '#' * 30)

        for advertisement in Handler.ADVERTISEMENTS:
            if advertisement.object_lists is not None:
                print(advertisement.__name__, advertisement.manager.counter())

        print('#' * 30, '\t Done \t', '#' * 30)

    @staticmethod
    def get_tickets():
        print('#' * 30, '\t List Tickets \t', '#' * 30)

        for advertisement in Handler.ADVERTISEMENTS:
            if advertisement.object_lists is not None:
                for ticket in advertisement.object_lists:
                    print(ticket)

        print('#' * 30, '\t Done \t', '#' * 30)

    @staticmethod
    def run():
        create_samples()

        for switch in Handler.SWITCHES:
            print(f'Press {switch} for {Handler.SWITCHES[switch]}')

        user_input = input('Please press your switch choice: ')
        if user_input.lower() == 'r':
            Handler.get_reports()
        elif user_input.lower() == 't':
            Handler.get_tickets()
        else:
            print('Invalid input')
            Handler.run()


if __name__ == '__main__':
    Handler.run()
