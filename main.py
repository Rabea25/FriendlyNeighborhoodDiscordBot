import asyncio
import os
from datetime import datetime, timedelta
import aladhan
from Tools.scripts.make_ctype import values
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
        channel = bot.get_channel(1298693730198622348)
        if channel:
            await channel.purge(limit=20)
            ctx = await bot.get_context(await channel.send("."))  # Fake message to create a context
            ctx.command = bot.get_command("prr")  # Set the command manually
            await bot.invoke(ctx)
        #await asyncio.sleep(time_until_midnight)


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

@bot.hybrid_command(name="testembed", with_app_command=True, description="test embed", aliases=["Testembed", "TESTEMBED"])
async def testembed(ctx: commands.Context):
    await ctx.defer(ephemeral=True)
    embed = discord.Embed(title="Prayer Times", description="Alexandria", color=discord.Color.green())
    embed.set_author(name="Ramadan Soon™️", icon_url='https://www.citypng.com/public/uploads/preview/png-ramadan-fanous-light-lantern-704081695045024fg4phtiihn.png')
    embed.set_footer(text="This is a footer")
    embed.add_field(name="Alexandria", inline=True, value="Fajr: 4:30 \nDhuhr: 12:30 \nAsr: 3:30 \nMaghrib: 6:30 \nIsha: 8:30")
    embed.add_field(name="Field 2", value="Value 2", inline=False)
    await ctx.reply(embed=embed)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
