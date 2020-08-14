from discord import Embed

class Embed_Builder():
    """
    Discordの埋め込みオブジェクトを作成するクラス
    """
    def __init__(self, title: str) -> None:
        self.embed = Embed(description=f"**{title}**")
    
    def add_values(self, title: str, values: list, inline=True) -> None:
        """
        フィールドに要素を改行区切りで追加する
        """
        self.embed.add_field(
            name=title,
            value="\n".join([str(v) for v in values]),
            inline=inline
        )