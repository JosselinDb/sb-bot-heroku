from discord_components.component import *

class SubjectsManager:
    """
        __ensures__

        __properties__

        __methods__
        
    """

    def __init__(self, list_fields : list) -> None:
        self._list_fields = list_fields


    def _find_field_by_id(self, id : str):
        return next((field for field in self._list_fields if field.id == id), None)


    def _find_subject_by_id(self, id_subject : str, id_field : str):
        field = self._find_field_by_id(id_field)

        if field is not None:
            return next((subject for subject in field.list_subjects if subject.id == id_subject), None)


    def get_labels_by_field(self, field_id : str):
        field = self._find_field_by_id(field_id)

        return [subject.label for subject in field.list_subjects]


    def _generate_subject_option(self, id_subject : str, id_field : str) -> SelectOption:
        subject = self._find_subject_by_id(id_subject, id_field)

        if subject is not None:
            return SelectOption(
                value=subject.id,
                label=subject.label,
                emoji=subject.emoji,
            )

    def generate_field_select(self, field_id : str) -> Select:

        field = self._find_field_by_id(field_id)

        select_options = list(
            map(
                lambda subject: self._generate_subject_option(subject.id, field_id),
                field.list_subjects
            )
        )

        return Select(
            options=select_options,
            id=field_id,
            placeholder=field.label,
            min_values=0,
            max_values=len(field.list_subjects)
        )

    def generate_all_selects(self):
        return [
            self.generate_field_select(field.id) for field in self._list_fields
        ]            

    