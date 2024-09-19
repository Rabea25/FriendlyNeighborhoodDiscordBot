import discord
from discord.ext import commands
from discord import app_commands

class Testme(commands.cog):
    def __init__(self, bot):
        self.bot = bot



async def setup(bot):
    await bot.add_cog(Testme(bot))