import discord
from discord.ext import commands

import config

bot = commands.Bot(command_prefix='!!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(config.privtoken)
