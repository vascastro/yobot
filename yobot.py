import discord
from discord.ext import commands

description = """
Olá! Eu sou Yobot, um bot criado pelo vascastro#9638!
"""

bot = commands.Bot(command_prefix='>', description=description)
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='Python'))

@bot.command()
async def teste(ctx):
    """Teste"""
    await ctx.send('Teste.', delete_after = 3.0)

bot.run('MzQ2MzM5MDI2ODYyODY2NDMy.DHIkkw.jG2zKdVegc9VNJmtn-QtFf0OMAQ')
