import discord, asyncio
from discord.ext import commands
from discord import app_commands
import aladhan

class APIS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("APIs cog loaded")



    @commands.hybrid_command(name='pr', with_app_command=True, aliases=["PR", "pR", "Pr"])
    async def pr(self, ctx):
        location = aladhan.City("Alexandria", "EG", "Egypt")
        client = aladhan.Client(location)
        x = client.get_today_times(location)
        for adhan in x:
            await ctx.send("{: <15} | {: <15}".format(adhan.get_en_name(), adhan.readable_timing(show_date=False)))




async def setup(bot):
    await bot.add_cog(APIS(bot))