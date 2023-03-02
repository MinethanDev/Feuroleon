#--- Importation discord.py
import discord
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async

#--- Création du bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), description="Quoi ? Feur.")

#--- Liste des "Quoi" possibles
quoilist = [
    "QUOI", "QUOI?", "QUOI ?", "QUOI!", "QUOI !", "QUOI.", "QUOI .", "QUOI-", "QUOI -",
    "KOI", "KOI?", "KOI ?", "KOI!", "KOI !", "KOI.", "KOI .", "KOI-", "KOI -",
    "TFK", "TFK?", "TFK ?", "TFK!", "TFK !", "TFK.", "TFK .", "TFK-", "TFK -",
    "PK", "PK?", "PK ?", "PK!", "PK !", "PK.", "PK .", "PK-", "PK -",
    "KWA", "KWA?", "KWA ?", "KWA!", "KWA !", "KWA.", "KWA .", "KWA-", "KWA -",
    "QWA", "QWA?", "QWA ?", "QWA!", "QWA !", "QWA.", "QWA .", "QWA-", "QWA -",
    "KUWA", "KUWA?", "KUWA ?", "KUWA!", "KUWA !", "KUWA.", "KUWA .", "KUWA-", "KUWA -",
    ]

#--- Recherche du "Quoi" utilisé
def search_quoi(message):
    messageup = message.content.upper()
    global repondre
    repondre = False
    for i in range(0, len(quoilist)):
        if messageup[-(len(quoilist[i])):] == quoilist[i]:
            print("IL A DIT QUOI !")
            repondre = True
            break


#--- Init
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='son coiffeur.'))
    print("Je suis prêt à Feuriser !") # Le bot est correctement initialisé

@bot.event
async def on_message(message):
    search_quoi(message)
    if repondre == True:
        quelquoi = randint(1,4)

        if quelquoi == 1:
            background = Editor("image.png")
            profile_image = await load_image_async(str(message.author.avatar.url))

            profile = Editor(profile_image).resize((340, 340)).circle_image().rotate(35, expand=True)

            background.paste(profile, (600, 650))

            file = File(fp=background.image_bytes, filename="feurmage.jpg")
            await message.reply("**Feur !**", mention_author=True, file=file)
            print("La personne a correctement été feurisée.")

        if quelquoi == 2:
            await message.reply("**-druplé !**", mention_author=True, file=discord.File("druple.png"))
            print("La personne a correctement été quadruplisée.")

        if quelquoi == 3:
            await message.reply("**-rtz !**", mention_author=True, file=discord.File("quartz.png"))
            print("La personne a correctement été quartzisée.")

        if quelquoi == 4:
            await message.reply("**-drilatère !**", mention_author=True, file=discord.File("drilatere.png"))
            print("La personne a correctement été quadrilatèrisée.")

        repondre == False

#--- Login au compte du bot
bot.run()
