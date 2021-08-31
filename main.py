
from controleurs.AdminManager import AdminManager
import controleurs.CommandManager

import discord
from discord_components import *
from discord.ext import commands
import os
import json

# Liste des préfixes du bot
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=["!admin ", "!dico ", "!exo ", "!rules "], intents=intents)
DiscordComponents(client)

# ______________________________
# Gestion des cogs

@controleurs.CommandManager.admin_command(AdminManager.admins)
@client.command()
async def load(ctx:commands.Context, extension:str) -> None: 
    """
        __ensures__
    Charge le cog avec le nom extension
    Réservée aux admins

        __parameters__
    :ctx: Contexte du message envoyé
    :extension: Nom du cog à charger

    """

    # charge le cog
    client.load_extension(f"cogs.{extension}")

@controleurs.CommandManager.admin_command(AdminManager.admins)
@client.command()
async def unload(ctx:commands.Context, extension:str) -> None:
    """
        __ensures__
    Décharge le cog avec le nom extension
    Réservée aux admins

        __parameters__
    :ctx: Contexte du message envoyé
    :extension: Nom du cog à décharger

    """

    # décharge le cog
    client.unload_extension(f"cogs.{extension}")

@controleurs.CommandManager.admin_command(AdminManager.admins)
@client.command()
async def reload(ctx:commands.Context, extension:str) -> None:
    """
        __ensures__
    Recharge le cog avec le nom extension
    Réservée aux admins

        __parameters__
    :ctx: Contexte du message envoyé
    :extension: Nom du cog à recharger

    """
    # décharge et charge le cog
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


# Chargement des cogs
for root, dirs, files in os.walk("./cogs"):
    for filename in files:
        root_name = root[2:].replace('/', '.')
        if filename.endswith(".py"):
            client.load_extension(f"{root_name}.{filename.split('.')[0]}")


# ______________________________
# Gestion du bot


# Connexion du bot
@client.event
async def on_ready():
    print('Logged on as {}'.format(client.user))
    

with open("config.json", "r") as f:
    data = json.load(f)
    SJtoken = data['tokens']['dev']['ShinJosselin']  # ShinJosselin
    SBtoken = data['tokens']['dev']['SBBot']  # SBBot
    PRODtoken = data['tokens']['prod']['SBBot']  # PROD SBBot

    client.run(PRODtoken)
