import asyncio
import os
from datetime import datetime, timedelta
import aladhan
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix='>', intents = intents, status=discord.Status.idle, activity=discord.Game("at being a silly Goose"))

    async def setup_hook(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')

        #await self.tree.sync(guild=discord.Object(id=892133019094241330))
        print("I hath synced")

    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral=True)



    async def on_ready(self):
        await scheduled_msg()
        print(f"{self.user} is up n runnin")



def chk(ctx):
    return ctx.author.id == 724770082479144971 or ctx.author.id == 599944573258694657 or ctx.author.guild_permissions.administrator

bot = Bot()

async def scheduled_msg():
    while True:
        now = datetime.now()
        next_midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        time_until_midnight = (next_midnight - now).total_seconds()
        print(time_until_midnight/60)
        await asyncio.sleep(time_until_midnight)
        location = aladhan.City("Alexandria", "EG", "Egypt")
        client = aladhan.Client(location)
        x = client.get_today_times(location)
        channel = bot.get_channel(1298693730198622348)
        await channel.purge(limit=5)
        for adhan in x:
            await channel.send("{: <15} | {: <15}".format(adhan.get_en_name(), adhan.readable_timing(show_date=False)))

@bot.hybrid_command(name="ping", with_app_command=True, description="Pong!", aliases=["Ping", "PING"])
async def ping(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    await ctx.reply(f"Pong! {round(bot.latency*1000)}ms")

@bot.hybrid_command(name="ban", with_app_command=True, description="Ban dat boy!", aliases=["Ban", "BAN"])
@commands.check(chk)
async def ban(ctx: commands.Context, member: discord.Member, *, reason=None):
    await ctx.defer(ephemeral=True)
    await ctx.guild.ban(member,reason=reason)
    await ctx.reply(f"Ban Hammer has fallen on {member.name}!", ephemeral=True)

@bot.hybrid_command(name="kick", with_app_command=True, description="Kick em to the ground!", aliases=["Kick", "KICK"])
@commands.check(chk)
async def kick(ctx: commands.Context, member: discord.Member, *, reason=None):
    await ctx.defer(ephemeral=True)
    await ctx.guild.kick(member,reason=reason)
    await ctx.reply(f"{member.name} has been curb stomped!")

@bot.hybrid_command(name="unban", with_app_command=True, description="its in the name", aliases=["Unban", "UNBAN"])
@commands.check(chk)
async def unban(ctx: commands.Context, member: discord.Member):
    await ctx.defer(ephemeral=True)
    await ctx.guild.unban(member)
    await ctx.reply(f"Unbanned {member.name}.")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
