from src import bot
from configparser import ConfigParser

if __name__ == "__main__":
    # settings.iniから設定を読み込みbotを起動
    config = ConfigParser()
    config.read("settings.ini")
    
    token = config["BOT"]["Token"]
    prefix = config["BOT"]["CommandPrefix"]

    bot = bot.TeamMakeBot(prefix)
    bot.run(token)