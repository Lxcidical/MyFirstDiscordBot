import discord
from discord.ext import commands

class Other(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot
### Kick CMD...
  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'Ping! `{round(client.latency * 1000)}ms`')
### Banning Group
  @commands.group(invoke_whitout_command=True)
  @commands.has_permission(ban_members=True)
  async def Banning(self, ctx):
    await ctx.send('This group contains commands that require permissions `ban_members`')
### Ban CMD...
  @group.command(aliases = "hammer")
  async def ban(ctx, member: commands.MemberConverter):
      await member.ban(member)
      await ctx.send(f'{member} has been banned!')

def setup(bot):
  bot.add_cog(Other(bot))
