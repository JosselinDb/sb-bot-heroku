import json

class AdminManager:
    """
        __ensures__
    Gère les administrateurs du bot
    Classe statique

        __attributes__
    admins : List<int>
        liste des administrateurs du bot

        __methods__
    add_admin(id, name) : None
        Ajoute un administrateur à la base
    get_admins() : List<int>
        Récupère la liste des administrateurs

    """

    with open("config.json", "r") as f:
        data = json.load(f)

        admins = data['admins']


    def __new__(cls) -> object:
        # Empêcher l'instanciation
        if cls is AdminManager:
            return None
    
        return object.__new__(cls)

    
