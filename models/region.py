from models.base import Base


class Region(Base):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.id} \t{self.name}'
