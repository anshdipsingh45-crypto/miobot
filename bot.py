import discord
from discord.ext import commands
import os

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

# Comando !social corretto
@bot.command()
async def social(ctx):
    messaggio = (
        "🌟 **Ecco i nostri canali ufficiali:**\n\n"
        "📱 **YouTube:** http://youtube.com\n"
        "🎮 **Twitch:** https://twitch.tv\n\n"
        "📌 *Seguici per non perderti le próximas dirette e i video!*"
    )
    await ctx.send(messaggio)

# Questa riga nasconde il token in modo sicuro
bot.run(os.environ.get('DISCORD_TOKEN'))
