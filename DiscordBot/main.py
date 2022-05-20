import discord
import random
import json
import asyncio
import datetime
from datetime import datetime
from config import *
from discord.ext import commands
import os

### Prefix
def get_prefix(client, message):
    with open('prefixes.json','r'):
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove():
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to "{prefix}".')
### Custom Help Command


### Bot Start-Up...
@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Game('Maxx is working on me rn...'))
    print("Bot is ready.")
  
client = commands.Bot(command_prefix=get_prefix, help_command=commands.MinimalHelpCommand())

###Moderation CMDS...
for filename in os.listdir('./cogs/lib/Moderation'): 
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
