#--- Importation discord.py
import discord
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async
from random import randint

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
            print("Présence de quoi détectée")
            repondre = True
            break

#--- Init
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='son coiffeur.'))
    print(bot.user.id)
    print("Je suis prêt à Feuriser !") # Le bot est correctement initialisé

@bot.event
async def on_message(message):
    msg = str(message.content)

    #--- Fonction QUOI FEUR
    search_quoi(message)
    if repondre == True:
        quelquoi = randint(1,5)

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

        if quelquoi == 5:
            await message.reply("**-rterback !**", mention_author=True, file=discord.File("rterback.png"))
            print("La personne a correctement été quarterbackisée.")

        repondre == False

    #--- Fonction Ca va le ...
    if str(message.author.id) != "1022158126818001017":
        if "CA VA" in msg.upper() or "ÇA VA" in msg.upper() or "CA VA?" in msg.upper() or "ÇA VA?" in msg.upper() or "CA VA ?" in msg.upper() or "ÇA VA ?" in msg.upper():
            auteur = str(message.author)
            await message.reply("Ca va et toi le " + auteur[0].upper(), mention_author=True)
            print("Ca va envoyé")
    
    #--- Fonction anti quoicoubeh
    if "QUOICOUBEH" in msg.upper():
        print("Quoicoubeh trouvé")
        await message.reply("**Tu es cringe**", mention_author=True, file=discord.File("cringe.gif"))
        print("Réponse au quoicoubeh envoyée")

#--- Login au compte du bot
bot.run("")
