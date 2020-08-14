from discord import Embed
from discord import embeds
from discord.ext import commands
from ..embed_builder import Embed_Builder

class CommandsCog(commands.Cog):
    """
    基本的なコマンド
    """
    def __init__(self, bot) -> None:
        self.bot = bot
        self.tm = bot.tm

    @commands.command()
    async def add(self, ctx, *names: str) -> None:
        """
        Botに名前を追加して、結果を表示する
        """
        # 名前が入力されていない場合その旨を出力する
        if len(names) == 0:
            await ctx.send("名前が入力されていません")
            return

        # メンバーの追加を試み、追加したメンバーとしていないメンバーに分ける
        added_members = []
        for name in names:
            try:
                self.tm.add_member(name)
                added_members.append(name)
            except ValueError:
                pass
        
        print(added_members)
        print(names)
        
        # 一人も追加しなかった場合その旨を出力して終了
        if len(added_members) == 0:
            await ctx.send("追加したメンバーはありません")
            return

        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("追加")
        eb.add_values("追加したメンバー", added_members)
        await ctx.send(embed=eb.embed)

    @commands.command()
    async def delete(self, ctx, *names: str) -> None:
        """
        Botに名前を追加して結果を表示する
        """
        # 名前が入力されていない場合その旨を出力して終了
        if len(names) == 0:
            await ctx.send("名前が入力されていません")
            return

        # メンバーの追加を試み、追加したメンバーとしていないメンバーに分ける
        deleted_members = []
        for name in names:
            try:
                self.tm.delete_member(name)
                deleted_members.append(name)
            except ValueError:
                pass

        # 一人も削除しなかった場合その旨を出力して終了
        if len(deleted_members) == 0:
            await ctx.send("削除したメンバーはありません")
            return

        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("削除")
        eb.add_values("削除したメンバー", deleted_members)
        await ctx.send(embed=eb.embed)

    @commands.command()
    async def clear(self, ctx) -> None:
        """
        チームメーカーにのメンバーを全て削除する
        """
        self.tm.clear_member()
        await ctx.send("全てのメンバーを削除しました")

    @commands.command(name="list")
    async def _list(self, ctx) -> None:
        """
        チームメーカーに追加済みのメンバーを表示する
        """
        members = self.tm.members
        
        # メンバーが登録されていない場合その旨を出力して終了
        if len(members) == 0:
            await ctx.send("メンバーが登録されていません")
            return
        
        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("表示")
        eb.add_values("追加済みのメンバー", members)
        await ctx.send(embed=eb.embed)

    @commands.command()
    async def make(self, ctx) -> None:
        """
        チーム分けをして表示する
        """
        # メンバーがチーム数より少ない場合その旨を出力して終了
        if len(self.tm.members) < self.tm.team_num:
            await ctx.send("メンバーが少なすぎます")
            return
        
        # チーム分け
        self.tm.make_team()

        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("チーム分け")
        # チームに分けられたメンバー
        for i, team in enumerate(self.tm.teams):
            eb.add_values(f"チーム{i+1}", team)
        # 余りのメンバー
        if len(self.tm.remainder) > 0:
            eb.add_values("余り", self.tm.remainder, inline=False)
        await ctx.send(embed=eb.embed)

    @commands.command()
    async def hello(self, ctx) -> None:
        await ctx.send("hello")

# Bot本体側からコグを読み込む際に呼び出される関数
def setup(bot):
    bot.add_cog(CommandsCog(bot))