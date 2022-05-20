import discord
from discord.ext import commands

class Moderation(commands.Cog): 
  
  def __init__(self, bot):
    self.bot = bot
### Kick CMD...
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(ctx, member: discord.Member,*,reason=None ):
      await member.kick(reason=reason)
      await ctx.send(f'{member} has been banned!')
### Purge CMD...
  @commands.command(aliases = "purge")
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount):
      await ctx.send('Unfinished Command...')

### Banning Group
  @commands.group(invoke_whitout_command=True)
  @commands.has_permission(ban_members=True)
  async def Banning(self, ctx):
    await ctx.send('This group contains commands that require permissions `ban_members`')
### Ban CMD...
  @Banning.command(aliases = "hammer")
  async def ban(ctx, member: discord.Member,*,reason=None):
      await member.ban(reason=reason)
      await ctx.send(f'{member} has been banned! Reason: `{reason}`')

def setup(bot):
  bot.add_cog(Moderation(bot))
