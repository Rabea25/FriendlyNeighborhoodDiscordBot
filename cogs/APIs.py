import discord, asyncio
from discord.ext import commands
from discord import app_commands
import requests, bs4, json

class APIS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("APIs cog loaded")



    @commands.hybrid_command(name='pr', with_app_command=True, aliases=["PR", "pR", "Pr"])
    async def pr(self, ctx, city='alex'):
        city = city.lower()
        url = "https://www.islamicfinder.org/world/egypt/361058/alexandria-prayer-times/"
        if city == 'cairo':
            url = "https://www.islamicfinder.org/world/egypt/360630/cairo-prayer-times/"
        elif city == 'kr' or city == 'daejeon':
            url = 'https://www.islamicfinder.org/world/republic-of-korea/1835235/daejeon-prayer-times/'
        elif city == 'ksa' or city == 'jeddah':
            url = 'https://www.islamicfinder.org/world/saudi-arabia/105343/jeddah-makkah-province-sa-prayer-times/'
        elif city == 'uae' or city == 'abudhabi' or city == 'ad':
            url = 'https://www.islamicfinder.org/world/united-arab-emirates/292968/abu-dhabi-abu-dhabi-ae-prayer-times/'

        soup = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
        names = [i.text for i in soup.find_all('span', class_='prayername')]
        times = [i.text for i in soup.find_all('span', class_='prayertime')]
        for p in zip(names, times):
            await ctx.send("{} - {}".format(p[0], p[1]))

async def setup(bot):
    await bot.add_cog(APIS(bot))