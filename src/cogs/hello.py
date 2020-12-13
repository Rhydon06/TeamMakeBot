from discord.ext import commands

class Hello(commands.Cog):
    """
    こんにちは
    """
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def hello(self, ctx) -> None:
        """
        挨拶をしましょう
        """
        await ctx.send(f"hello {ctx.author.display_name}")

# Bot本体側からコグを読み込む際に呼び出される関数
def setup(bot):
    bot.add_cog(Hello(bot))