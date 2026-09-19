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

# Comando !ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Comando !social corretto con gli "a capo" e i link funzionanti
@bot.command()
async def social(ctx):
    messaggio = (
        "🌟 **Ecco i nostri canali ufficiali:**\n\n"
        "📱 **YouTube:** http://www.youtube.com/@GISCU-h4y\n"
        "🎮 **Twitch:** https://twitch.tv\n\n"
        "📌 *Seguici per non perderti le prossime dirette e i video!*"
    )
    await ctx.send(messaggio)

# Il tuo token è perfetto e inserito correttamente
bot.run('MTU1MDc5MTk3ODM3ODMzODMzNA.GqRAXg.HrenqW0byl0jPm7O0Iy06Xvfb5AjKetxsdYFcg')
