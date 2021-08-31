class Classe:
    """
        __ensures__

        __properties__

        __methods__
    """

    def __init__(self, id : str, title : str, emoji : str) -> None:
        self._id = id
        self._title = title
        self._emoji = emoji
    
    @property
    def id(self):
        return self._id
        
    @property
    def title(self):
        return self._title

    @property
    def emoji(self):
        return self._emoji