import re
import discord
from discord.ext.commands.context import Context
from discord.ext.commands.core import check
from discord_components import component
from discord_components.interaction import Interaction
from administration.ClassesManager import ClassesManager
from administration.modeles.Level import Level
from administration.modeles.Classe import Classe
from administration.SignsManager import SignsManager
from administration.modeles.Sign import Sign
from administration.SubjectsManager import SubjectsManager
from administration.modeles.Subject import Subject
from administration.modeles.Field import Field
from administration.RolesManager import RolesManager
import controleurs.CommandManager
from tools.colors import Color, colors


from discord import Embed, emoji
from discord.ext import commands

import asyncio


class Administration(commands.Cog):
    """
    Adminsitration

        __attributes__
        
        __methods__

        __commands__

        __listener__
    on_ready
    on_button_click
    on_select_option
    """

    # ______________________________
    # Initialisation

    def __init__(self, client) -> None:
        self.client = client
        self.client.remove_command("help")  # commande help par défaut

        self.signs_manager = SignsManager(Administration._signs())
        self.classes_manager = ClassesManager(Administration._levels())
        self.subjects_manager = SubjectsManager(Administration._fields())


    @staticmethod
    def _signs():
        rules = Sign(
            "rules",
            "Règlement",
            colors[Color.BLURPLE],
            "https://duboisj.iiens.net/images/regulation-icon-blurple.png",
            # "https://icon-library.com/images/regulation-icon/regulation-icon-19.jpg",
            articles_file="./administration/sources/rules.txt"
        )

        ask_for_help = Sign(
            "ask_for_help",
            "À propos des demandes d'aide",
            colors[Color.YELLOW],
            "https://duboisj.iiens.net/images/writing-icon-yellow.png",
            # "https://cdn.iconscout.com/icon/free/png-512/writing-15-156169.png",
            articles_file="./administration/sources/ask_for_help.txt"
        )

        welcome_to_SB = Sign(
            "welcome_to_SB",
            "Bienvenue sur School Booster",
            colors[Color.RED],
            "https://image.flaticon.com/icons/png/512/167/167707.png",
            content="""
            **School Booster** est un serveur d'**entraide**, ayant pour but de t'aider à t'**épanouir** et à **performer** scolairement.

            Que ce soit pour de l'**aide aux devoirs**, des **questions d'orientations**, pour faire parler ta **flamme pédagogique**, ou simplement pour **te détendre et discuter**, School Booster est l'endroit idéal.
            """
        )

        start_ur_journey = Sign(
            "start_journey",
            "Commence ton séjour !",
            colors[Color.YELLOW],
            "https://icons-for-free.com/iconfiles/png/512/idea+idea+bulb+light+bulb+icon-1320144733751939202.png",
            content="""
            Pour commencer, nous t'invitons à lire le <#860519842305540112> pour que le serveur soit le plus agréable pour tous !
            
            Tu pourras ensuite te rendre dans <#860519842305540114> pour pouvoir accéder aux salons d'aide.

            Et si jamais tu rencontres un quelconque problème, n'hésites pas à contacter nos <@&860519842305540109>.
            """
        )

        return [rules, ask_for_help, welcome_to_SB, start_ur_journey]

    @staticmethod
    def _levels():
        # 📙📕📗📘
        # 🖍️🖊️🖋️
        # 🏚️🏠🏫🏢🏰
        # 🧑‍🔬🧑‍💼

        sixieme = Classe('6e', 'Sixième', '📙')
        cinquieme = Classe('5e', 'Cinquième', '📕')
        quatrieme = Classe('4e', 'Quatrième', '📗')
        troisieme = Classe('3e', 'Troisième', '📘')

        seconde = Classe('snd', 'Seconde', '🖍️')
        premiere = Classe('prm', 'Première', '🖊️')
        terminale = Classe('tle', 'Terminale', '🖋️')

        bp1 = Classe('bp1', 'Bac+1', '🏚️')
        bp2 = Classe('bp2', 'Bac+2', '🏠')
        bp3 = Classe('bp3', 'Bac+3', '🏫')
        bp4 = Classe('bp4', 'Bac+4', '🏢')
        bp5 = Classe('bp5', 'Bac+5', '🏰')

        these = Classe('ths', 'Thèse', '🧑‍🔬')
        vie_active = Classe('vact', 'Vie active', '🧑‍💼')

        college = Level('clg', 'Collège', '🏚️', 1, [sixieme, cinquieme, quatrieme, troisieme])
        lycee = Level('lyc', 'Lycée', '🏠', 3, [seconde, premiere, terminale])
        superieur = Level('spr', 'Supérieur', '🏫', 4, [bp1, bp2, bp3, bp4, bp5])
        au_dela = Level('adl', 'Au-delà', '🏢', 2, [these, vie_active])

        return [college, lycee, superieur, au_dela]

    @staticmethod
    def _fields():
        # 🔢 🔭 ⚗️ 🌱 💻 🖥️ 🔩
        # 🏺 🌍 ⚖ 📈
        # 📚 📕
        # 🇬🇧 🇪🇸 🇩🇪 🇯🇵

        maths = Subject('maths', 'Mathématiques', '🔢')
        physics = Subject('physics', 'Physique', '🔭')
        chemistry = Subject('chemistry', 'Chimie', '⚗️')
        biology = Subject('biology', 'SVT', '🌱')
        computer_science = Subject('computer_science', 'Informatique', '💻')
        technology = Subject('technology', 'Technologie', '🖥️')
        engineering = Subject('engineering', 'Sciences de l\'ingénieur', '🔩')

        history = Subject('history', 'Histoire', '🏺')
        geography = Subject('geography', 'Géographie', '🌍')
        socialogy = Subject('socialogy', 'Sciences sociales', '⚖')
        economy = Subject('economy', 'Économie', '📈')

        french = Subject('french', 'Français', '📚')
        philosophy = Subject('philosophy', 'Philosophie', '📕')

        english = Subject('english', 'Anglais', '🇬🇧')
        spanish = Subject('spanish', 'Espagnol', '🇪🇸')
        deutsch = Subject('deutsch', 'Allemand', '🇩🇪')
        japanese = Subject('japanese', 'Japonais', '🇯🇵')
        italian = Subject('italian', 'Italien', '🇮🇹')
        chinese = Subject('chinese', 'Chinois', '🇨🇳')
        arabic = Subject('arabic', 'Arabe', '☪️')

        scientific_subjects = [maths, physics, chemistry, biology, computer_science, technology, engineering]
        scientific = Field("scientific", "Scientifique", scientific_subjects)

        social_subjects = [history, geography, socialogy, economy]
        social = Field("social", "Économique et social", social_subjects)

        litterature_subjects = [french, philosophy]
        litterature = Field("litterature", "Littéraire", litterature_subjects)

        languages_subjects = [english, spanish, deutsch, japanese, italian, chinese, arabic]
        languages = Field("languages", "Langues", languages_subjects)

        return [scientific, social, litterature, languages]
 

    @commands.Cog.listener()
    async def on_ready(self):
        print("Administration disponible")


    @commands.Cog.listener()
    async def on_button_click(self, interaction : Interaction):
        # Classes management

        if (interaction.component.id == "cres"):
            embed = Embed(
                title = "Correspondance des systèmes francophones",
                description="",
                colour=colors[Color.GRAY]
            )
            embed.set_image(url="https://i.imgur.com/U6L9T8J.png")
        
            await interaction.respond(embed=embed)


    @commands.Cog.listener()
    async def on_select_option(self, interaction : Interaction):
        # Classes management

        print(interaction.values)

        if interaction.component.id == "classes":

            classe = self.classes_manager.find_classe_by_id_without_level(interaction.values[0])
            classe_label = classe.title

            member = interaction.guild.get_member(interaction.user.id)

            await RolesManager.add_unique_roles(member, self.classes_manager.list_classes_labels, classe_label)
            await interaction.respond(content=f"Le rôle `{classe_label}` t'as bien été ajouté")

        # Subjects management
        else:

            field_id = interaction.component.id
            field_label = self.subjects_manager._find_field_by_id(field_id).label

            all_field_subjects_labels = self.subjects_manager.get_labels_by_field(field_id)

            subjects_labels = list(
                map(
                    lambda value: self.subjects_manager._find_subject_by_id(value, field_id).label,
                    interaction.values
                )
            )

            member = interaction.guild.get_member(interaction.user.id)

            await RolesManager.add_unique_roles(member, all_field_subjects_labels, *subjects_labels)

            
            if len(subjects_labels) > 0:
                await interaction.respond(
                    content=f"Tu as obtenu les rôles {', '.join(subjects_labels)}"
                )
            else:
                await interaction.respond(
                    content=f"Tu n'as pas pris de rôle de la catégorie {field_label}"
                )


    @controleurs.CommandManager.admin_command()
    @commands.guild_only()
    async def launch_sign(self, ctx : commands.Context, id = "all") -> None:
        await ctx.message.delete()

        if id == "all":
            for sign in self.signs_manager.list_signs:
                await ctx.send(embed = self.signs_manager.sign_to_embed(sign.id))

            return

        embed = self.signs_manager.sign_to_embed(id)
        
        if embed is None:
            await ctx.send(embed = Embed(
                title="Aucun panneau ne correspond à l'identifiant " + id,
                description="",
                colour=colors[Color.RED]
            ))

        else:
            await ctx.send(embed = embed)


    @controleurs.CommandManager.admin_command()
    @commands.guild_only()
    async def launch_classes(self, ctx : commands.Context):
        await ctx.message.delete()

        embed = Embed(
            title="Choisis ta classe",
            description="Utilise le menu déroulant pour que le rôle correspondant te soit automatiquement attribué.\n\nEn cas de difficultés, n'hésite pas à contacter un modérateur ou administrateur.",
            color=colors[Color.RED]
        )
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/274/backpack_1f392.png")

        correspondance_button = [component.Button(label="Autre système ? Voir les correspondances", emoji="📋", style=2, id="cres")]

        components = [self.classes_manager.generate_full_select(), correspondance_button]

        await ctx.send(embed=embed, components=components)


    @controleurs.CommandManager.admin_command()
    @commands.guild_only()
    async def launch_helper(self, ctx : commands.Context):
        await ctx.message.delete()

        embed = Embed(
            title="Deviens helper ?",
            description="Si tu es désireux d'aider les autres sur ce serveur, choisis tes matières à l'aide des différentes listes déroulantes pour pouvoir te signaler aux autres membres.\n\nEn cas de difficultés, n'hésite pas à contacter un modérateur ou administrateur.",
            color=colors[Color.YELLOW]
        )
        embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/274/graduation-cap_1f393.png")

        components = self.subjects_manager.generate_all_selects()

        await ctx.send(embed=embed, components=components)

        
# Initialisation du cog
def setup(client):
    client.add_cog(Administration(client))
