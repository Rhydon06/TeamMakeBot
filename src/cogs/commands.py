from typing import List
from src.team_maker.team_maker import TeamMaker
from discord import Member, Guild
from discord.ext import commands
from ..embed_builder import Embed_Builder

# TODO
MAX_VALUE_LEN = 12

class Commands(commands.Cog):
    """
    基本的なコマンド
    """
    def __init__(self, bot) -> None:
        self.bot = bot
        self.tm: TeamMaker = bot.tm

    def names_from_members(self, members, guild: Guild):
        members = [guild.get_member(member.id) for member in members]
        # names = list(map(lambda member: f"{member.display_name} {member.id}", members))
        names = [member.display_name for member in members]
        return names

    @commands.command()
    async def add(self, ctx: commands.Context, *members: Member) -> None:
        """
        Botにメンバーを追加する
        """

        # 名前が入力されていない場合自分を追加する
        if len(members) == 0:
            members = [ctx.author]

        # メンバーの追加を試み、追加したメンバーとしていないメンバーに分ける
        added_members = []
        for member in members:
            try:
                self.tm.members_deleted.discard(member.id)
                self.tm.members_not_deleted.add(member.id)
                self.tm.add_member(member.id)
                added_members.append(member.display_name)
            except ValueError:
                pass
        
        # 一人も追加しなかった場合その旨を出力して終了
        if len(added_members) == 0:
            await ctx.send("追加したメンバーはありません")
            return

        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("追加")
        eb.add_values("追加したメンバー", added_members, MAX_VALUE_LEN)
        await ctx.send(embed=eb.embed)

    @commands.command()
    async def delete(self, ctx: commands.Context, *members: Member) -> None:
        """
        Botから指定したメンバーを削除する
        """
        # 名前が入力されていない場合自分を削除する
        if len(members) == 0:
            members = [ctx.author]

        # メンバーの削除を試み、削除したメンバーとしていないメンバーに分ける
        deleted_members = []
        for member in members:
            try:
                self.tm.members_deleted.add(member.id)
                self.tm.members_not_deleted.discard(member.id)
                self.tm.delete_member(member.id)
                deleted_members.append(member.display_name)
            except ValueError:
                pass

        # 一人も削除しなかった場合その旨を出力して終了
        if len(deleted_members) == 0:
            await ctx.send("削除したメンバーはありません")
            return

        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("削除")
        eb.add_values("削除したメンバー", deleted_members, MAX_VALUE_LEN)
        await ctx.send(embed=eb.embed)

    @commands.command()
    async def clear(self, ctx: commands.Context) -> None:
        """
        Botに追加されているメンバーを全て削除する
        """
        self.tm.clear_member()
        self.tm.members_deleted = set()
        self.tm.members_not_deleted = set()
        await ctx.send("全てのメンバーを削除しました")

    @commands.command(name="list")
    async def _list(self, ctx: commands.Context) -> None:
        """
        Botに追加済みのメンバーを表示する
        """

        # TODO
        names = self.names_from_members(self.tm.members, ctx.guild)

        # メンバーが登録されていない場合その旨を出力して終了
        if len(names) == 0:
            await ctx.send("メンバーが登録されていません")
            return
        
        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("表示")
        eb.add_values("追加済みのメンバー", names, MAX_VALUE_LEN)
        await ctx.send(embed=eb.embed)

    @commands.command()
    async def make(self, ctx: commands.Context) -> None:
        """
        チーム分けをする
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
            names = self.names_from_members(team, ctx.guild)
            eb.add_values(f"チーム{i+1}", names, MAX_VALUE_LEN)
        # 余りのメンバー
        if self.tm.remainder:
            names = self.names_from_members(self.tm.remainder, ctx.guild)
            eb.add_values("余り", names, MAX_VALUE_LEN, inline=False)
        await ctx.send(embed=eb.embed)

    @commands.command()
    async def addvc(self, ctx: commands.Context) -> None:
        """
        送信者と同じボイスチャンネルに接続している人をBotに追加する
        """
        # 送信者が接続しているボイスチャンネル
        voice = ctx.author.voice

        # ボイスチャンネルに接続中でない場合、その旨を送信し終了
        if not voice:
            await ctx.send("ボイスチャンネルに入って実行してください")
            return

        # ボイスチャンネルに接続中のメンバーの表示名
        members: List[Member] = voice.channel.members

        # メンバーの追加を試み、追加したメンバーとしていないメンバーに分ける
        added_members = []
        for member in members:
            try:
                self.tm.add_member(member.id)
                added_members.append(member.display_name)
            except ValueError:
                pass
        
        # 一人も追加しなかった場合その旨を出力して終了
        if len(added_members) == 0:
            await ctx.send("追加したメンバーはありません")
            return

        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("追加")
        eb.add_values("追加したメンバー", added_members, MAX_VALUE_LEN)
        await ctx.send(embed=eb.embed)

    @commands.command()
    async def makevc(self, ctx: commands.Context) -> None:
        """
        ボイスチャンネルに接続している人だけでチーム分けをする
        """
        # 送信者が接続しているボイスチャンネル
        voice = ctx.author.voice

        # ボイスチャンネルに接続中でない場合、その旨を送信し終了
        if not voice:
            await ctx.send("ボイスチャンネルに入って実行してください")
            return

        # ボイスチャンネルに接続中のメンバーの表示名
        members: List[Member] = voice.channel.members
        ids = set([member.id for member in members])

        for member in self.tm.members:
            if member.id not in ids:
                try:
                    self.tm.delete_member(member.id)
                except ValueError:
                    pass

        # メンバーの追加
        for member in members:
            try:
                self.tm.add_member(member.id)
            except ValueError:
                pass
        
        # チーム分け
        self.tm.make_team()

        # Discordに表示される埋め込みオブジェクトの作成と送信
        eb = Embed_Builder("チーム分け")
        for i, team in enumerate(self.tm.teams):
            names = self.names_from_members(team, ctx.guild)
            eb.add_values(f"チーム{i+1}", names, MAX_VALUE_LEN)
        if self.tm.remainder:
            names = self.names_from_members(self.tm.remainder, ctx.guild)
            eb.add_values("余り", names, MAX_VALUE_LEN, inline=False)
        await ctx.send(embed=eb.embed)


# Bot本体側からコグを読み込む際に呼び出される関数
def setup(bot):
    bot.add_cog(Commands(bot))