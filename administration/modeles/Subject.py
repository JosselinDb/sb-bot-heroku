class Subject:
    """
        __ensures__

        __properties__

        __methods__
    """

    def __init__(self, id : str, label : str, emoji : str) -> None:
        self._id = id
        self._label = label
        self._emoji = emoji

    
    @property
    def id(self):
        return self._id
        
    @property
    def label(self):
        return self._label

    @property
    def emoji(self):
        return self._emoji