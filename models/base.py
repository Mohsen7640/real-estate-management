from abc import ABC

from models.manager import Manager


class Base(ABC):
    _id = 0
    object_lists = None
    manager = None

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.store(self)
        self.set_manager()

        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def store(cls, obj):
        if cls.object_lists is None:
            cls.object_lists = list()
        cls.object_lists.append(obj)

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)
