bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run('NDQ2MTQ1Njg1MTkzMDk3MjI2.Dd1zzg.nFyskkj31NdFYKCk-pm3HMrWad8')
