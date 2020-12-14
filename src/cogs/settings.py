from src.team_maker.team_maker import TeamMaker
from discord.ext import commands
from ..embed_builder import Embed_Builder

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
    
    @commands.command()
    async def fix(self, ctx, *names: str) -> None:
        """
        指定したメンバーが余りにならないようにする
        """
        # 名前が入力されていない場合その旨を出力する
        if len(names) == 0:
            await ctx.send("名前が入力されていません")
            return

        # メンバーの固定を試み、固定したメンバーとしていないメンバーに分ける
        fixed_members = []
        for name in names:
            try:
                self.tm.fix(name)
                fixed_members.append(name)
            except ValueError:
                pass
        
        # 一人も固定しなかった場合その旨を出力して終了
        if len(fixed_members) == 0:
            await ctx.send("固定したメンバーはありません")
            return

        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("固定")
        eb.add_values("固定したメンバー", fixed_members)
        await ctx.send(embed=eb.embed)
    
    @commands.command()
    async def unfix(self, ctx, *names: str) -> None:
        """
        指定したメンバーの固定状態を解除する
        """
        # 名前が入力されていない場合その旨を出力する
        if len(names) == 0:
            await ctx.send("名前が入力されていません")
            return

        # メンバーの固定の解除を試み、固定を解除したメンバーとしていないメンバーに分ける
        unfixed_members = []
        for name in names:
            try:
                self.tm.unfix(name)
                unfixed_members.append(name)
            except ValueError:
                pass
        
        # 一人も固定解除しなかった場合その旨を出力して終了
        if len(unfixed_members) == 0:
            await ctx.send("固定を解除したメンバーはありません")
            return

        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("固定を解除")
        eb.add_values("固定を解除したメンバー", unfixed_members)
        await ctx.send(embed=eb.embed)

# Bot本体側からコグを読み込む際に呼び出される関数
def setup(bot):
    bot.add_cog(Settings(bot))