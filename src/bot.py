from discord.ext import commands

class TeamMakeBot(commands.Bot):
    """
    Bot本体
    run(トークン)で起動する
    """

    def __init__(self, command_prefix: str):
        """
        discord上で入力するコマンドの接頭語を設定する
        """
        print("bot起動中…")
        super().__init__(command_prefix)
    
    async def on_ready(self):
        """
        botの準備完了時に呼び出される
        """
        print("-----")
        print("bot準備完了")
        print("name: " + self.user.name)
        print("id: " + str(self.user.id))
        print("-----")