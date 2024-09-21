import discord
from discord.ext import commands
from discord import app_commands

def chckwin(board):
    if board[0]==board[1]==board[2]!='~':
        return board[2]
    if board[3]==board[4]==board[5]!='~':
        return board[5]
    if board[6]==board[7]==board[8]!='~':
        return board[6]
    if board[0]==board[3]==board[6]!='~':
        return board[0]
    if board[1]==board[4]==board[7]!='~':
        return board[1]
    if board[2]==board[5]==board[8]!='~':
        return board[2]
    if board[0]==board[4]==board[8]!='~':
        return board[0]
    if board[2]==board[4]==board[6]!='~':
        return board[2]

    return '~'


class xogame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("xogame cog loaded")

    @commands.hybrid_command(name="twopxo", with_app_command=True, aliases=["XO", "Xo", "xO"])
    async def twopxo(self, ctx, member: discord.Member, member2: discord.Member):
        playerss = [member, member2]
        board = ['~', '~', '~', '~', '~', '~', '~', '~', '~']
        await ctx.reply("welcome to my mini Tic Tac Toe, please note that the cells are numbered like this")
        await ctx.send("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")
        win = 0
        flag = True
        for turn in range(1,10):
            player = 'O'
            if turn%2:
                player = 'X'
            await ctx.send("enter where you want to play from 1 to 9")
            await ctx.send(board[0] + " | " + board[1] + " | " + board[2] + '\n' + board[3] + " | " + board[4] + " | " + board[5] +'\n' + board[6] + " | " + board[7] + " | " + board[8])
            num = await self.bot.wait_for('message', check=lambda message: message.author == playerss[(turn+1)%2])
            num = int(num.content)
            while num<1 or num>9 or board[num-1] != '~':
                await ctx.send('invalid, please enter an empty cell')
                num = await self.bot.wait_for('message', check=lambda message: message.author == playerss[(turn+1)%2])
                num = int(num.content)
            board[num-1] = player
            x = chckwin(board)
            if x != '~':
                if x == 'X':
                    await ctx.send(f"Congratulations! {member} wins.")
                else:
                    await ctx.send(f"Congratulations! {member2} wins.")
                flag = False
                break
        if flag:
            x = chckwin(board)
            if x != '~':
                if x == 'X':
                    await ctx.send(f"Congratulations! {member} wins.")
                else:
                    await ctx.send(f"Congratulations! {member2} wins.")
            else:
                await ctx.send("nobody won, losers.")



async def setup(bot):
    await bot.add_cog(xogame(bot))

