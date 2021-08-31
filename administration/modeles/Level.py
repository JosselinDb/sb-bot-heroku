class Level:
    """
        __ensures__
    
        __properties__

        __methods__

    """

    def __init__(self, id : str, title : str, emoji : str, style : int, list_classes : list) -> None:
        self._id = id
        self._title = title
        self._emoji = emoji
        self._style = style  # 1: blurple ; 2:grey ; 3:green ; 4:red ; 5:url
        self._list_classes = list_classes

    @property
    def id(self):
        return self._id
    
    @property
    def emoji(self):
        return self._emoji
    
    @property
    def title(self):
        return self._title
    
    @property
    def style(self):
        return self._style
    
    @property
    def list_classes(self):
        return self._list_classes