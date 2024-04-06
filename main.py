# Importations bibliothèques
import discord
import config
from emojis import decode
from random import randint, choice
from string import punctuation
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async

# Déclaration du bot & du client
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Init
@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='son coiffeur.'))
    print("Feuroléon a correctement démarré et est connecté à Discord.")

# Liste des "QUOI" possibles
quoilist = ["quoi", "koi", "tfk", "pk", "kwa", "qwa", "kuwa", "quwa"]

# Fonction Feur
@bot.event
async def on_message(message):

    str_msg = decode(message.content.strip(punctuation + ' ').lower())

    mots = str_msg.split()
    
    for mot in mots:
        if mot[0] == ":" and mot[-1] == ":":
            mots.remove(mot)

    str_msg = ''.join(mots)

    for quoi in quoilist:
        if str_msg.endswith(quoi):
            print("'Quoi' trouvé dans le message '{0}' de {1}".format(str_msg, message.author))
            quelquoi = randint(1, 5)

            if quelquoi == 1:
                background = Editor("assets/coiffeur.png")
                profile_image = await load_image_async(message.author.avatar.url)
                profile = Editor(profile_image).resize((340, 340)).circle_image().rotate(15, expand=True)
                background.paste(profile, (650, 685))
                file = File(fp=background.image_bytes, filename="feurmage.jpg")
                await message.reply("**Feur !**", mention_author=True, file=file)
                print("Réponse envoyée à {0} avec Feur".format(message.author))

            if quelquoi == 2:
                await message.reply("**-druplé !**", mention_author=True, file=discord.File("assets/druple.png"))
                print("Réponse envoyée à {0} avec Quadruplé".format(message.author))

            if quelquoi == 3:
                await message.reply("**-rtz !**", mention_author=True, file=discord.File("assets/quartz.png"))
                print("Réponse envoyée à {0} avec Quartz".format(message.author))

            if quelquoi == 4:
                await message.reply("**-drilatère !**", mention_author=True, file=discord.File("assets/drilatere.png"))
                print("Réponse envoyée à {0} avec Quadrilatère".format(message.author))

            if quelquoi == 5:
                await message.reply("**-rterback !**", mention_author=True, file=discord.File("assets/rterback.png"))
                print("Réponse envoyée à {0} avec Quarterback".format(message.author))

    if "uwu" in str_msg:
        print("UwU trouvé dans le message '{0}' de {1}".format(str_msg, message.author))
        await message.reply("", mention_author=True, file=discord.File("assets/uwu.mp4"))
        print("UwU envoyé à {0}".format(message.author))

    if "quoicoubeh" in str_msg:
        print("'Quoicoubeh' trouvé dans le message '{0}' de {1}".format(str_msg, message.author))
        await message.reply("**Tu es cringe**", mention_author=True, file=discord.File("assets/cringe.gif"))
        print("'Quoicoubeh' envoyé à {0}".format(message.author))

# Commande /question
@bot.tree.command(name="question", description="Posez une question fermée et Feuroléon y répondra")
async def questioncmd(interaction: discord.Interaction, votre_question: str):
    await interaction.response.send_message("{0} me demande : **{1}**\nJe lui répond : **{2}** !".format("<@" + str(interaction.user.id) + ">", votre_question, choice(["Oui", "Non", "Peut-être", "Probablement", "Probablement pas", "Impossible", "Surement"])))
    print("Commande question utilisée par {0}".format(interaction.user.name))

# Commande /orthographe
@bot.tree.command(name="orthographe", description="Épinglez quelqu'un pour son orthographe désastreuse")
async def orthographe(interaction: discord.Interaction, coupable: discord.Member):
    await interaction.response.send_message("{0} je t'informe que {1} a signalé ton orthographe désastreuse...".format("<@" + str(coupable.id) + ">", "<@" + str(interaction.user.id) + ">"), file=discord.File("assets/bescherelle.jpg"))
    print("Commande orthographique utilisée par {0} sur {1}".format(interaction.user.name, coupable))

# Commande /cringe
@bot.tree.command(name="cringe", description="Dénoncez une personne beaucoup trop cringe")
async def cringe(interaction: discord.Interaction, coupable: discord.Member):
    await interaction.response.send_message("**{0} VOUS ÊTES EN ÉTAT D'ARRESTATION POUR EXCÈS DE CRINGE !**\nMerci {1} de dénoncer ces dangereux criminels.".format("<@" + str(coupable.id) + ">", "<@" + str(interaction.user.id) + ">"), file=discord.File("assets/police.jpg"))
    print("Commande anti-cringe utilisée par {0} sur {1}".format(interaction.user.name, coupable))

# Commande /feur
@bot.tree.command(name="feur", description="Feuriser quelqu'un !")
async def feur(interaction: discord.Interaction, victime: discord.Member):
    background = Editor("assets/coiffeur.png")
    profile_image = await load_image_async(victime.avatar.url)
    profile = Editor(profile_image).resize((340, 340)).circle_image().rotate(15, expand=True)
    background.paste(profile, (650, 685))
    file = File(fp=background.image_bytes, filename="feurmage.jpg")
    await interaction.response.defer()
    await interaction.followup.send(content=f"**Feur ! {victime.mention}**", file=file)

# Commande /mariage
@bot.tree.command(name="mariage", description="Mariez deux personnes entre elles !")
async def mariage(interaction: discord.Interaction, romeo: discord.Member, juliette: discord.Member):
    background = Editor("assets/mariage.png")
    profile_image = await load_image_async(romeo.avatar.url)
    profile = Editor(profile_image).resize((200, 200)).circle_image()
    background.paste(profile, (603, 108))
    profile_image = await load_image_async(juliette.avatar.url)
    profile = Editor(profile_image).resize((200, 200)).circle_image()
    background.paste(profile, (360, 160))
    file = File(fp=background.image_bytes, filename="felicitations.jpg")
    await interaction.response.defer()
    await interaction.followup.send(content=f"**Vive les mariés :partying_face:\n{romeo.mention} :heart: {juliette.mention}**", file=file)

# Exécution du bot
bot.run(config.BOT_TOKEN)
