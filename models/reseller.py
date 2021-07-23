from models.base import Base


class Reseller(Base):

    def __init__(self, first_name, last_name, phone_number, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

        super().__init__(*args, **kwargs)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.id}\t {self.fullname}\t {self.phone_number}'
