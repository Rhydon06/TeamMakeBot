from src.team_maker.team_maker import TeamMaker
from discord.ext import commands

class Settings(commands.Cog):
    """
    設定
    """
    def __init__(self, bot) -> None:
        self.bot = bot
        self.tm: TeamMaker = bot.tm

    @commands.command()
    async def tnum(self, ctx, num: str) -> None:
        """
        チーム数を変更する
        """
        try:
            num = int(num)
        except ValueError:
            await ctx.send("整数を入力してください")
            return
        
        if num < 2:
            await ctx.send("値が小さすぎます")

        self.tm.team_num = num

        await ctx.send(f"チーム数を {num} に変更しました")
    
    @commands.command()
    async def tsize(self, ctx, size: str) -> None:
        """
        1チームの人数を変更する
        """
        try:
            size = int(size)
        except ValueError:
            await ctx.send("整数を入力してください")
            return
        
        if size < 2:
            await ctx.send("値が小さすぎます")

        self.tm.team_size = size

        await ctx.send(f"1チームの人数を {size} に変更しました")
    
# Bot本体側からコグを読み込む際に呼び出される関数
def setup(bot):
    bot.add_cog(Settings(bot))