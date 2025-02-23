from time import sleep

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
        if city == 'Cairo':
            url = "https://www.islamicfinder.org/world/egypt/360630/cairo-prayer-times/"
        elif city == 'kr' or city == 'daejeon':
            city = 'Daejeon'
            url = 'https://www.islamicfinder.org/world/republic-of-korea/1835235/daejeon-prayer-times/'
        elif city == 'ksa' or city == 'jeddah':
            city = 'Jeddah'
            url = 'https://www.islamicfinder.org/world/saudi-arabia/105343/jeddah-makkah-province-sa-prayer-times/'
        elif city == 'uae' or city == 'abudhabi' or city == 'ad':
            city = 'Abu Dhabi'
            url = 'https://www.islamicfinder.org/world/united-arab-emirates/292968/abu-dhabi-abu-dhabi-ae-prayer-times/'
        elif city == 'fayoum':
            url = 'https://www.islamicfinder.org/world/egypt/42607115/fayoum-prayer-times/'
            city = 'Fayoum'
        elif city == 'giza':
            url = 'https://www.islamicfinder.org/world/egypt/360995/giza-prayer-times/'
            city = 'Giza'
        else:
            city = 'Alexandria'
        soup = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
        names = [i.text for i in soup.find_all('span', class_='prayername')]
        times = [i.text for i in soup.find_all('span', class_='prayertime')]
        #for p in zip(names, times):
        #    await ctx.send("{} - {}".format(p[0], p[1])) \
        await ctx.defer(ephemeral=True)
        embed = discord.Embed(title="Prayer Times", color=discord.Color.random())
        embed.set_author(name="Ramadan Soon™️", icon_url='https://www.citypng.com/public/uploads/preview/png-ramadan-fanous-light-lantern-704081695045024fg4phtiihn.png')
        embed.add_field(name=city, inline=True,
                        value=f"Fajr: {times[0]} \nSunrise: {times[1]} \nDhuhr: {times[2]} \nAsr: {times[3]} \nMaghrib: {times[4]} \nIsha: {times[5]}")
        await ctx.reply(embed=embed)

    @commands.hybrid_command(name='prr', with_app_command=True)
    async def prr(self, ctx):
        cities = [['Alexandria', "https://www.islamicfinder.org/world/egypt/361058/alexandria-prayer-times/"],
                  ['Cairo', "https://www.islamicfinder.org/world/egypt/360630/cairo-prayer-times/"],
                  ['Giza', 'https://www.islamicfinder.org/world/egypt/360995/giza-prayer-times/'],
                  ['Daejeon', 'https://www.islamicfinder.org/world/republic-of-korea/1835235/daejeon-prayer-times/'],
                  ['Jeddah', 'https://www.islamicfinder.org/world/saudi-arabia/105343/jeddah-makkah-province-sa-prayer-times/'],
                  ['Abu Dhabi', 'https://www.islamicfinder.org/world/united-arab-emirates/292968/abu-dhabi-abu-dhabi-ae-prayer-times/'],
                  ['Fayoum', 'https://www.islamicfinder.org/world/egypt/42607115/fayoum-prayer-times/']]

        embed = discord.Embed(title="Prayer Times", color=discord.Color.random())
        embed.set_author(name="Ramadan Soon™️",
                         icon_url='https://www.citypng.com/public/uploads/preview/png-ramadan-fanous-light-lantern-704081695045024fg4phtiihn.png')
        await ctx.defer(ephemeral=True)
        await ctx.reply("Processing...")
        for city in cities:
            req = requests.get(city[1])
            if req.status_code == 200:
                soup = bs4.BeautifulSoup(req.text, 'html.parser')
                names = [i.text for i in soup.find_all('span', class_='prayername')]
                times = [i.text for i in soup.find_all('span', class_='prayertime')]
                embed.add_field(name=city[0], inline=True,
                                value=f"Fajr: {times[0]} \nSunrise: {times[1]} \nDhuhr: {times[2]} \nAsr: {times[3]} \nMaghrib: {times[4]} \nIsha: {times[5]}")
                await asyncio.sleep(0.5)
        await ctx.channel.purge(limit=1)
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(APIS(bot))