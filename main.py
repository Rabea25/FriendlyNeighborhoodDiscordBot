import os
import asyncio
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
Bot = discord.Client(intents=discord.Intents.all(), status=discord.Status.online,
                     activity=discord.Game("at being a silly Goose"), command_prefix=">")
tree = app_commands.CommandTree(Bot)


@Bot.event
async def on_ready():
    print('up n runnin')
    await tree.sync()


@tree.command(name="ping")
async def ping(interaction: discord.Integration):
    await interaction.response.send_message('pong! {} ms'.format(round(Bot.latency * 1000)))


Bot.run(token=TOKEN)
