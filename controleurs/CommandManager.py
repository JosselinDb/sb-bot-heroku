from controleurs.AdminManager import AdminManager
from discord.ext.commands import Context, command
from functools import wraps


def __general_command(aliases : list, prefix : str, user_restriction = []) -> object:
    """
        __ensures__
    Décorateur: vérifie que la commande utilise le bon préfixe :prefix:
    Donne les alias :aliases: à la commande

        __returns__
    Le décorateur

        __parameters__
    aliases : les alias du nom de la commande décorée
    prefix : le préfixe à vérifier pour la commande

    """

    def decorator(function : object) -> object:
        
        @command(aliases=aliases)  # définit une commande, avec comme alias :aliases:
        @wraps(function)  # garde le nom
        async def wrapper(slf : object, ctx : Context, *args, **kwargs) -> None:
            if ctx.prefix != prefix:
                return
            
            if user_restriction != [] and ctx.author.id not in user_restriction:
                return

            await function(slf, ctx, *args, **kwargs)
        
        return wrapper
    
    return decorator


def admin_command(admins = AdminManager.admins, aliases = []) -> object:
    """ cf __general_command : cas particulier pour la commande !admin """
    return __general_command(aliases, "!admin ", admins)


def rules_command(admins = [], aliases = []) -> object:
    """ cf __general_command : cas particulier pour la commande !rules """
    return __general_command(aliases, "!rules ", admins)