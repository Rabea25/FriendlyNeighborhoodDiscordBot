import discord
from discord.ext import commands
from discord import app_commands

class Testme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("test cog loaded")

    @commands.hybrid_command(name="ping2", with_app_command=True)
    async def ping2(self, ctx):
        await ctx.reply("lakad haremna mn agl hazeh el la7za")



async def setup(bot):
    await bot.add_cog(Testme(bot))