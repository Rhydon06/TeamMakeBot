from discord import Intents
from discord.ext import commands
from .team_maker.team_maker import TeamMaker

# コグのあるフォルダ
COGS_FOLDER = "src.cogs"

# コグ
COGS = [
    "commands",
    "test_cog"
]

class TeamMakeBot(commands.Bot):
    """
    Bot本体
    run(トークン)で起動する
    """

    def __init__(self, command_prefix: str) -> None:
        print("bot起動中…")
        
        # discordに入力するコマンドの接頭語を設定
        super().__init__(command_prefix=command_prefix, intents=Intents.all())

        # チームメーカー
        self.tm = TeamMaker()

        # コグの読み込み
        for cog in COGS:
            self.load_extension(f"{COGS_FOLDER}.{cog}")

    
    async def on_ready(self) -> None:
        """
        botの準備完了時に呼び出される
        """
        print("-----")
        print("bot準備完了")
        print("name: " + self.user.name)
        print("id: " + str(self.user.id))
        print("-----")