from discord.ext import commands
import discord

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Loaded: Example')

    @commands.command()
    async def ping(self, ctx):
        """Returns the bot's latency."""
        embed = discord.Embed(
            title='🏓 Pong!',
            description=f'Latency: {round(self.bot.latency * 1000)}ms',
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def hello(self, ctx):
        """Greets the user."""
        await ctx.send(f'Hello, {ctx.author.name}!')

async def setup(bot):
    await bot.add_cog(Example(bot))
