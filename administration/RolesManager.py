from os import stat
from discord import Member
from discord.utils import get

class RolesManager:
    """
    
    """

    @staticmethod
    def _get_role_by_label(member : Member, label : str):
        return get(member.guild.roles, name=label)


    @staticmethod
    def _get_roles_by_labels(member : Member, labels : list):
        return list(map(
            lambda label: RolesManager._get_role_by_label(member, label),
            labels)
        )


    @staticmethod
    async def add_unique_roles(member : Member, all_roles_labels : list, *roles_labels : list):
        to_add_roles = RolesManager._get_roles_by_labels(member, roles_labels)
        all_roles = RolesManager._get_roles_by_labels(member, all_roles_labels)

        to_remove_roles = [role for role in member.roles if role in all_roles]

        for to_remove_role in to_remove_roles:
            await member.remove_roles(to_remove_role)

        await member.add_roles(*to_add_roles)


    @staticmethod
    async def add_roles_witouth_duplicates(member : Member, roles_labels : list):
        roles = RolesManager._get_roles_by_labels(member, roles_labels)
        to_add_roles = [role for role in roles if role not in member.roles]

        await member.add_roles(*to_add_roles)