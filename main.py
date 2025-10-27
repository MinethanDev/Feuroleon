#################################################################
# Projet : Feuroléon                      Création : 21.09.2022 #
# Auteur : Minethan                           Fichier : main.py #
# Description : Bot Discord humoristique répondant "Feur" à un  #
#               message finissant par "Quoi", ainsi que         #
#               d'autres fonctionnalités                        #
# Version : 2.5                                                 #
#################################################################

#--------------------[ Importation des bibliothèques
import discord
import config
from emojis import decode
from random import randint, choice
from string import punctuation
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async

#--------------------[ Initialisation et démarrage du bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)                                                                       

@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='son coiffeur.'))
    print(f'{bot.user} a correctement démarré et est connecté à Discord.')

#--------------------[ Fonction exécutée à chaque message
@bot.event
async def on_message(message):

    if message.author.bot:
        return

    mots = decode(message.content.strip(punctuation + ' ').lower()).split()
    mots = [m for m in mots if not (m.startswith(":") and m.endswith(":"))]
    str_msg = ''.join(mots)

    if len(str_msg) >= 2 and any(str_msg.endswith(q) for q in config.liste_quoi):
        print(f"'Quoi' trouvé dans le message '{str_msg}' de {message.author}")

        choix = randint(1, 5)
        texte, image, avatar = config.reps_feur[choix]

        if avatar:
            background = Editor(image)
            profile_image = await load_image_async(message.author.avatar.url)
            profile = (
                Editor(profile_image)
                .resize((340, 340))
                .circle_image()
                .rotate(15, expand=True)
            )
            background.paste(profile, (650, 685))
            file = File(fp=background.image_bytes, filename="feurmage.jpg")
        else:
            file = discord.File(image)

        await message.reply(texte, mention_author=True, file=file)
        print(f"Réponse envoyée à {message.author} avec {texte.strip('*')}")

    if "uwu" in str_msg:
        await message.reply("", mention_author=True, file=discord.File("assets/uwu.mp4"))
        print("UwU envoyé à {0}".format(message.author))

    if "quoicoubeh" in str_msg:
        await message.reply("**Tu es cringe**", mention_author=True, file=discord.File("assets/cringe.gif"))
        print("'Quoicoubeh' envoyé à {0}".format(message.author))

    await bot.process_commands(message)

#--------------------[ Commande /question
@bot.tree.command(name="question", description="Posez une question fermée et Feuroléon y répondra")
async def question(interaction: discord.Interaction, votre_question: str):
    print("Commande question utilisée par {0}".format(interaction.user.name))
    await interaction.response.send_message(
        "{0} me demande : **{1}**\nJe lui répond : **{2}** !".format(
            "<@" + str(interaction.user.id) + ">", votre_question, choice(config.reps_question)))

#--------------------[ Commande /orthographe
@bot.tree.command(name="orthographe", description="Épinglez quelqu'un pour son orthographe désastreuse")
async def orthographe(interaction: discord.Interaction, coupable: discord.Member):
    print("Commande orthographique utilisée par {0} sur {1}".format(interaction.user.name, coupable))
    await interaction.response.send_message(
        "{0} je t'informe que {1} a signalé ton orthographe désastreuse...".format(
            "<@" + str(coupable.id) + ">", "<@" + str(interaction.user.id) + ">"), file=discord.File("assets/bescherelle.jpg"))

#--------------------[ Commande /cringe
@bot.tree.command(name="cringe", description="Dénoncez une personne beaucoup trop cringe")
async def cringe(interaction: discord.Interaction, coupable: discord.Member):
    print("Commande anti-cringe utilisée par {0} sur {1}".format(interaction.user.name, coupable))
    await interaction.response.send_message(
        "**{0} VOUS ÊTES EN ÉTAT D'ARRESTATION POUR EXCÈS DE CRINGE !**\nMerci {1} de dénoncer ces dangereux criminels.".format(
            "<@" + str(coupable.id) + ">", "<@" + str(interaction.user.id) + ">"), file=discord.File("assets/police.jpg"))

#--------------------[ Commande /feur
@bot.tree.command(name="feur", description="Feuriser quelqu'un !")
async def feur(interaction: discord.Interaction, victime: discord.Member):
    await interaction.response.defer()
    background = Editor("assets/coiffeur.png")
    profile_image = await load_image_async(victime.avatar.url)
    profile = Editor(profile_image).resize((340, 340)).circle_image().rotate(15, expand=True)
    background.paste(profile, (650, 685))
    file = File(fp=background.image_bytes, filename="feurmage.jpg")
    await interaction.followup.send(content=f"**Feur ! {victime.mention}**", file=file)

#--------------------[ Commande /mariage
@bot.tree.command(name="mariage", description="Mariez deux personnes entre elles !")
async def mariage(interaction: discord.Interaction, romeo: discord.Member, juliette: discord.Member):
    await interaction.response.defer()
    background = Editor("assets/mariage.png")
    profile_image = await load_image_async(romeo.avatar.url)
    profile = Editor(profile_image).resize((200, 200)).circle_image()
    background.paste(profile, (603, 108))
    profile_image = await load_image_async(juliette.avatar.url)
    profile = Editor(profile_image).resize((200, 200)).circle_image()
    background.paste(profile, (360, 160))
    file = File(fp=background.image_bytes, filename="felicitations.jpg")
    await interaction.followup.send(content=f"**Vive les mariés :partying_face:\n{romeo.mention} :heart: {juliette.mention}**", file=file)

#--------------------[ Commande /talk
@bot.tree.command(name="talk", description="Parler via Feuroléon (réservé au développeur)")
async def talk(interaction: discord.Interaction):

    if interaction.user.id != config.id_dev:
        await interaction.response.send_message("J'te parle pas à toi")
        return
    
    await interaction.response.send_message("Check tes mp.", ephemeral=True)
    
    try:
        dm = await interaction.user.create_dm()
        await dm.send("Quel message dois-je envoyer ?")

        def check(msg):
            return msg.author == interaction.user and isinstance(msg.channel, discord.DMChannel)

        response = await bot.wait_for('message', check=check)

        await interaction.channel.send(f"{response.content}")

    except discord.errors.Forbidden:
        await interaction.response.send_message("Je n'ai pas pu envoyer de message privé.", ephemeral=True)
        
#--------------------[ Exécution du bot
bot.run(config.BOT_TOKEN)