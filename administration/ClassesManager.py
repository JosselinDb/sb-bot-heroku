from discord_components.component import *

class ClassesManager:
    """
        __ensures__

        __properties__

        __methods__
        
    """

    def __init__(self, list_levels : list) -> None:
        self._list_levels = list_levels
        self._list_classes_labels = self._list_labels()

    @property
    def list_levels(self):
        return self._list_levels

    @property
    def list_classes_labels(self):
        return self._list_classes_labels


    def _list_labels(self):
        labels = []
        for level in self.list_levels:
            labels += [classe.title for classe in level.list_classes]

        return labels

    def _find_level_by_id(self, id : str):
        return next((level for level in self.list_levels if level.id == id), None)
    

    def _find_classe_by_id(self, id_level : str, id_classe : str):

        level = self._find_level_by_id(id_level)

        if level is not None:
            return next((classe for classe in level.list_classes if classe.id == id_classe), None)


    def find_classe_by_id_without_level(self, id_classe : str):

        for level in self.list_levels:
            
            classe = self._find_classe_by_id(level.id, id_classe)
            if classe is not None:
                return classe



    def _generate_classe_option(self, id_level : str, id_classe : str) -> SelectOption:
        classe = self._find_classe_by_id(id_level, id_classe)

        if classe is not None:
            return SelectOption(
                value=classe.id,
                label=classe.title,
                emoji=classe.emoji,
            )


    def generate_full_select(self) -> Select:

        options = []
        for level in self.list_levels:

            select_options = list(
                map(
                    lambda classe: self._generate_classe_option(level.id, classe.id),
                    level.list_classes
                )
            )

            options += select_options

        return Select(
            options=options,
            id="classes",
            placeholder="Choisis ta classe",
            min_values=1,
            max_values=1
        )