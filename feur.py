#--- Importation discord.py
import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO

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

        background = Image.open("image.png")
        data = BytesIO(await message.author.display_avatar.read())
        pfp = Image.open(data)
        pfp = pfp.resize((340,340))
        background.paste(pfp, (650, 720))
        background.save("profile.jpg")

        await message.reply("**Feur !**", mention_author=True, file=discord.File('profile.jpg'))
        print("La personne a correctement été feurisée.")
        repondre == False

#--- Login au compte du bot
bot.run()