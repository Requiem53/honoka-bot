import discord
import os
import subprocess
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
# Define bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Start the Minecraft server
@bot.command(name="start")
async def start_server(ctx):
    await ctx.send("Starting the Minecraft server...")

    # Check if the server is already running
    result = subprocess.run(["pgrep", "-f", "minecraft_server.jar"], capture_output=True, text=True)
    if result.stdout.strip():
        await ctx.send("Minecraft server is already running!")
        return

    # Start server using tmux
    subprocess.run(["tmux", "new-session", "-d", "-s", "minecraft", "java -Xms1G -Xmx4G -jar server.jar nogui"])
    await ctx.send("Minecraft server started!")

# Run the bot
bot.run(TOKEN)
