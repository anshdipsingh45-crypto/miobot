import discord
from discord.ext import commands

# Configurazione dei permessi (Intents)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

# Creazione del bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Il bot {bot.user} è online e pronto!")

# Comando !ping (Rimane attivo!)
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Comando !social aggiornato solo con YouTube e Twitch
@bot.command()
async def social(ctx):
    messaggio = (
        "🌟 **Ecco i nostri canali ufficiali:**\n\n"
        "📱 **YouTube:** http://www.youtube.com/@GISCU-h4y"
        "🎮 **Twitch:** twitch.tv/giscu_official"
        "📌 *Seguici per non perderti le prossime dirette e i video!*"
    )
    await ctx.send(messaggio)

# Incolla il tuo Token qui sotto
bot.run('MTU1MDc5MTk3ODM3ODMzODMzNA.GwWFHL.4ytDDyFBdodPGa1NDCNCYT4QdUui8TlTS1xUIA
')
