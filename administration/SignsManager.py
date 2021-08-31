import re
from discord import Embed
from discord_components import *

from administration.modeles.Sign import Sign


class SignsManager:
    """
        __ensures__
    Gère les messages de règles et d'informations relatives aux demandes d'aides

        __attributes__
    list_signs : list[Sign]
        La liste des panneaux qu'on veut manipuler

        __methods__
    to_embed(sign) : Embed
        Retourne l'embed correspondant au panneau
    """


    def __init__(self, list_signs : list) -> None:
        self._list_signs = list_signs

    @property
    def list_signs(self):
        return self._list_signs
    
    @list_signs.setter
    def list_signs(self, value):
        self._list_signs = value

    def add_sign(self, sign : Sign):
        self.list_signs = self.list_signs + [sign]


    

    def sign_to_embed(self, id : str):
        """
            __ensures__
        récupère et renvoit l'embed correspondant au panneau de l'id renseigné

            __parameters__
        id : l'id du panneau recherché
        """
        sign = next((s for s in self.list_signs if s.id == id), None)

        if sign is not None:
            return self._to_embed(sign)
 

    def _to_embed(self, sign : Sign):
        """
            __ensures__
        Créé l'embed à partir des paramètres du panneau
        """
        
        sign_embed = Embed(
            title=sign.title,
            description=sign.description,
            color=sign.color
        )

        sign_embed.set_thumbnail(url=sign.image_url)

        return sign_embed
    