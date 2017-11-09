import discord
from discord.ext import commands

auth_tags = {}

class tag:
    """Comandos matemáticos."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def tag(self, ctx, tag = None):
        """Mostra comando de tag."""
        if tag is not None:
            await ctx.message.delete()
            await ctx.send(auth_tags[tag])
        else:
            await ctx.send('```Utilize o comando de tag da seguinte forma:``````!tag add/info nome```')

    @tag.command(name = 'add')
    async def add(self, ctx, tag, descript):
        """Adiciona uma tag ao banco."""
        if tag == 'add' or tag == 'info':
            await ctx.send('Você não pode adicionar uma tag com o nome add.')
            return
        try:
            auth_tags.update({tag:descript})
            await ctx.send ('```Tag adicionada ao banco com sucesso. Utilize !tag {}.```'.format(tag))
        except Exception as err:
            print (err)

def setup(bot):
    bot.add_cog(tag(bot))
