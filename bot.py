import discord
from discord.ext import commands
import datetime, re
from cogs.creds import *

description = """
Olá! Eu sou Yobot, um bot criado pelo vascastro#9638!
"""

def _prefix_callable(bot, msg):
    prefix = '!'
    return prefix

initial_extensions = [
    'cogs.avisos',
    'cogs.dbtools',
    'cogs.poll',
    'cogs.maths',
    'cogs.moderation',
    'cogs.welcome',
    'cogs.tag',
]

class Yobot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=_prefix_callable, description=description,
                         pm_help=None, help_attrs=dict(hidden=True))

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
                print(extension + ' loaded succesfully.')
            except Exception as e:
                print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    def run(self):
        super().run(yobot, reconnect=True)

    async def on_ready(self):
        if not hasattr(self, 'uptime'):
            self.uptime = datetime.datetime.utcnow()
        print(f'Ready: {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        await bot.process_commands(message)

bot = Yobot()
bot.run()
