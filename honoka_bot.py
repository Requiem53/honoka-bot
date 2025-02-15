import discord
import os
import subprocess
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
# Define bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

#Start the Minecraft server
@bot.command(name="start")
async def start_server(ctx):
    await ctx.send("Starting the Minecraft server... Wait, okay?\n https://tenor.com/view/love-live-school-idol-project-honoka-kousaka-trumpet-honk-gif-19422260")

    # Check if the server is already running
    result = subprocess.run(["pgrep", "-f", "server.jar"], capture_output=True, text=True)
    if result.stdout.strip():
        await ctx.send("Minecraft server is already running desu yo!! https://tenor.com/view/umi-honoka-gif-25604008")
        return

    # Start server using tmux
    subprocess.run(["tmux", "new-session", "-d", "-s", "minecraft", "java -Xms2G -Xmx4G -jar server.jar nogui"])
    await ctx.send("Minecraft server started!! Let's play!! https://tenor.com/view/lets-goo-honoka-kousaka-gif-23293886")

@bot.command(name="fd")
async def faitodayo(ctx):
    await ctx.send("Faito dayo!! \nhttps://tenor.com/view/honoka-kosaka-love-live-dance-gif-22348813")


@bot.command(name="whoisstupid")
async def whoisstupid(ctx):
    await ctx.send("Hmmmmm I think Raphael Chase Osorio from Pardo Cebu City near 7/11!! \n https://tenor.com/view/honoka-anime-gif-5514844")
# Run the bot
bot.run(TOKEN)
