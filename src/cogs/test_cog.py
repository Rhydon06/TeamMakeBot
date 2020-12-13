from discord.ext import commands

class TestCog(commands.Cog):
    """
    基本的なコマンド
    """
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def hello(self, ctx) -> None:
        await ctx.send(f"hello {ctx.author.display_name}")

# Bot本体側からコグを読み込む際に呼び出される関数
def setup(bot):
    bot.add_cog(TestCog(bot))