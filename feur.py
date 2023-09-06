#--- Importation discord.py
import discord
import random
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async

#--- Création du bot
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all(), description="Quoi ? Feur.")

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

#--- Liste des "Ca va" possibles
cavalist = [
    "CA VA", "CA VA?", "CA VA ?",
    "ÇA VA", "ÇA VA?", "ÇA VA ?",
    "CAVA", "CAVA?", "CAVA ?",
    "ÇAVA", "ÇAVA?", "ÇAVA ?",
    "SAVA", "SAVA?", "SAVA ?",
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
    msgup = str(msg.upper())

    #--- Fonction QUOI FEUR
    search_quoi(message)
    if repondre == True:
        quelquoi = random.randint(1,5)

        if quelquoi == 1:
            background = Editor("assets/coiffeur.png")
            profile_image = await load_image_async(str(message.author.avatar.url))

            profile = Editor(profile_image).resize((340, 340)).circle_image().rotate(35, expand=True)

            background.paste(profile, (600, 650))

            file = File(fp=background.image_bytes, filename="feurmage.jpg")
            await message.reply("**Feur !**", mention_author=True, file=file)
            print("La personne a correctement été feurisée.")

        if quelquoi == 2:
            await message.reply("**-druplé !**", mention_author=True, file=discord.File("assets/druple.png"))
            print("La personne a correctement été quadruplisée.")

        if quelquoi == 3:
            await message.reply("**-rtz !**", mention_author=True, file=discord.File("assets/quartz.png"))
            print("La personne a correctement été quartzisée.")

        if quelquoi == 4:
            await message.reply("**-drilatère !**", mention_author=True, file=discord.File("assets/drilatere.png"))
            print("La personne a correctement été quadrilatèrisée.")

        if quelquoi == 5:
            await message.reply("**-rterback !**", mention_author=True, file=discord.File("assets/rterback.png"))
            print("La personne a correctement été quarterbackisée.")

        repondre == False

    #--- Fonction Ca va le ...
    if str(message.author.id) != "1022158126818001017":
        for i in range (len(cavalist)):
            if cavalist[i] == msg.upper():
                auteur = str(message.author)
                await message.reply("Ça va et toi le " + auteur[0].upper() + " ?", mention_author=True)
                print("Ca va envoyé")
    
    #--- Fonction anti quoicoubeh
    if "QUOICOUBEH" in msg.upper():
        print("Quoicoubeh trouvé")
        await message.reply("**Tu es cringe**", mention_author=True, file=discord.File("assets/cringe.gif"))
        print("Réponse au quoicoubeh envoyée")

    #--- Fonction Indochine
    if "A LA VIE, A Y CROIRE" in msg.upper():
        print("Indo'ref trouvée")
        await message.reply("**A NOS CÉLÉBRATIOOOONS**", mention_author=True, file=discord.File("assets/celebrations.gif"))
        print("A NOS CELEBRATIOOOONS")

    #--- Fonction Voyance
    if msgup.startswith('DIS MOI FEUROLÉON') or msgup.startswith('DIS MOI FEUROLEON'):
        print("Question de voyance trouvée")
        reponses = ['Oui', 'Non', 'Peut-être', 'La réponse D', 'Probablement', 'Probablement pas', 'Surement', 'Impossible', "J'm'en branle"]
        reponse = random.choice(reponses)
        await message.reply(reponse, mention_author=True)
        print("Réponse envoyée")

    #--- Fonction Voyance Bescherelle édition
    if msgup.startswith('DIT MOI FEUROLÉON') or msgup.startswith('DIT MOI FEUROLEON'):
        print("Question de voyance mal orthographiée trouvée")
        reponses = ['Oui', 'Non', 'Peut-être', 'Probablement', 'Probablement pas', 'Surement', 'Impossible', "J'm'en branle"]
        reponse = random.choice(reponses)
        await message.reply(reponse + " mais va apprendre à conjuguer s'il te plaît.", mention_author=True, file=discord.File("assets/bescherelle.jpg"))
        print("Réponse envoyée")
       

    #--- Fonction Echelle
    if msgup.startswith('SUR UNE ÉCHELLE DE 1 A 10') or msgup.startswith('SUR UNE ÉCHELLE DE 1 À 10') or msgup.startswith('SUR UNE ECHELLE DE 1 A 10') or msgup.startswith('SUR UNE ECHELLE DE 1 À 10'):
        print("Question d'échelle trouvée")
        await message.reply(random.randint(1, 10), mention_author=True)
        print("Échelle envoyée")

    #--- Fonction UwU
    if "UWU" in msg.upper():
        print("UwU trouvé")
        await message.reply("", mention_author=True, file=discord.File("assets/uwu.mp4"))
        print("Réponse au UwU envoyée")
    
    #--- Fonction Mariage
    if msgup.startswith('FEUROLÉON MARIE MOI') or msgup.startswith('FEUROLEON MARIE MOI'):
        print("Demande en mariage détectée")
        mariageoupas = random.randint(1,2)

        if mariageoupas == 1:
            await message.reply("", mention_author=True, file=discord.File("assets/bsrnon.jpg"))

        if mariageoupas == 2:
            background = Editor("assets/mariage.png")
            profile_image = await load_image_async(str(message.author.avatar.url))

            profile = Editor(profile_image).resize((340, 340)).circle_image()

            background.paste(profile, (650, 320))

            file = File(fp=background.image_bytes, filename="mariagefinal.jpg")
            await message.reply("**Oui je le veux**", mention_author=True, file=file)

        print("Réponse au mariage envoyée")

#--- Login au compte du bot
bot.run("MTAyMjE1ODEyNjgxODAwMTAxNw.Ggui4X.ZTYDdWnfpIVwvx_6E_uqAPkBk2Yh-3jsQRxx-8")