class Field:
    """
        __ensures__
    
        __properties__

        __methods__

    """

    def __init__(self, id : str, label : str, list_subjects : list) -> None:
        self._id = id
        self._label = label
        self._list_subjects = list_subjects

    @property
    def id(self):
        return self._id
    
    @property
    def label(self):
        return self._label
    
    @property
    def list_subjects(self):
        return self._list_subjects