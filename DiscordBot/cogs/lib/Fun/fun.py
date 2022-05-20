import discord
import random
from discord.ext import commands

class Fun(commands.Cog): 
    
  def __init__(self, bot):
    self.bot = bot
### 8ball CMD
responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]
  @commands.command()
  async def eightball(ctx, question):
      await ctx.send(random(responses))
  @commands.group(invoke_whitout_command=True)
  async def fungroup(ctx):
      await ctx.send('This is a group for other...')
  @group.command()
  async def funsub(ctx):
    await ctx.send('This is a group command for other....')

def setup(bot):
  bot.add_cog(Fun(bot))
