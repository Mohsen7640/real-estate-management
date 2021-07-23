class Manager:

    def __init__(self, _class=None):
        self._class = _class

    def counter(self):
        """
        return size object_lists
        :return: int
        """
        return len(self._class.object_lists)

    def search(self, **kwargs):
        """
        :param kwargs: area__min=80, area__max=200, built_year__min=1393
        :return: list
        """
        search_result = list()
        for key, value in kwargs.items():
            if key.endswith('__min'):
                key = key[:-5]
                compare_key = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare_key = 'max'
            else:
                key = key
                compare_key = 'equal'

            if search_result:
                self._class.object_lists.clear()
                for obj in search_result:
                    self._class.object_lists.append(obj)
                search_result.clear()

            for obj in self._class.object_lists:
                if hasattr(obj, key):
                    if compare_key == 'min':
                        result = getattr(obj, key) >= value
                    elif compare_key == 'max':
                        result = getattr(obj, key) <= value
                    else:
                        result = getattr(obj, key) == value

                    if result:
                        search_result.append(obj)

        return search_result

    def get(self, **kwargs):
        search_result = None

        for key, value in kwargs.items():
            if key.endswith('__min'):
                key = key[:-5]
                compare_key = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare_key = 'max'
            else:
                key = key
                compare_key = 'equal'

            if search_result:
                self._class.object_lists.clear()
                self._class.object_lists.append(search_result)
                search_result = None

            for obj in self._class.object_lists:
                if hasattr(obj, key):
                    if compare_key == 'min':
                        result = getattr(obj, key) >= value
                    elif compare_key == 'max':
                        result = getattr(obj, key) <= value
                    else:
                        result = getattr(obj, key) == value

                    if result:
                        search_result = obj

        return search_result
