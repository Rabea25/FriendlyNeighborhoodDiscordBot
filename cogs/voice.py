import discord, asyncio
from discord.ext import commands
from discord import app_commands
import ffmpeg, subprocess, json

def get_audio_length(filepath: str) -> float:
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', filepath],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    info = json.loads(result.stdout)
    return float(info['format']['duration'])

def imowner(ctx):
    return ctx.author.id == 724770082479144971
class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Voice cog loaded")

    @commands.hybrid_command(name='eih', with_app_command=True)
    @commands.check(imowner)
    async def eih(self, ctx):
        vc = ctx.author.voice.channel
        if ctx.voice_client is not None:
            ctx.voice_client.disconnect()
        await vc.connect()
        audio_source = discord.FFmpegPCMAudio('./VoiceSamples/eih.wav')  # Replace 'url' with the file path
        print(ctx.voice_client.play(audio_source))
        len = get_audio_length('./VoiceSamples/eih.wav')+1
        await asyncio.sleep(len+0.5)
        await ctx.voice_client.disconnect()

async def setup(bot):
    await bot.add_cog(Voice(bot))