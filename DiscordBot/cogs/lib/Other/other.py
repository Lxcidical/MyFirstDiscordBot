import discord
from discord.ext import commands

class Other(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot
### Kick CMD...
  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'Ping! `{round(client.latency * 1000)}ms`')

  @commands.group(invoke_whitout_command=True)
  async def othergroup(ctx):
      await ctx.send('This is a group for other...')
  @group.command()
  async def othersub(ctx):
    await ctx.send('This is a group command for other....')

def setup(bot):
  bot.add_cog(Other(bot))
