from discord import Embed

DEFAULT_MAX_VALUE_LEN = 100

class Embed_Builder():
    """
    Discordの埋め込みオブジェクトを作成するクラス
    """
    def __init__(self, title: str) -> None:
        self.embed = Embed(description=f"**{title}**")
    
    def add_values(self, title: str, values: list,
        max_value_len: int=DEFAULT_MAX_VALUE_LEN, inline=True) -> None:
        """
        フィールドに要素を改行区切りで追加する
        """
        self.embed.add_field(
            name=title,
            value="\n".join([self.__value_format(v, max_value_len) for v in values]),
            inline=inline
        )

    def __value_format(self, value, length: int) -> str:
        if len(str(value)) <= length:
            return str(value)
        return str(value)[:length-1]+"…"