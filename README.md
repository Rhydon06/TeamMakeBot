# TeamMakeBot
Discord上でランダムなチーム分けを行うことが出来るBotです。   
バグがあったら教えてください。


# 環境設定
1. 最新のPython3をインストール([python.org](https://www.python.org/))
2. discord.pyをインストール([詳しい説明](https://discordpy.readthedocs.io/ja/latest/intro.html))
3. DiscordのBotアカウントを作成し、Botを使いたいサーバーに招待([詳しい説明](https://discordpy.readthedocs.io/ja/latest/discord.html))
4. [Discord開発者ポータル](https://discord.com/developers/applications)->Applications->設定するBot->Botタブの順に移動して、Privileged Gateway Intentsの直下のボタンを2つオンにする([詳しい説明](https://qiita.com/disneyresidents/items/72741a88265107dd04d3))
5. **settings.ini**の**Token**の値に、作成したBotアカウントのトークンを設定


# 起動方法
**bot_run.py**を実行

# よくある使い方
## ボイスチャンネルにいる人達でランダムにチーム分けをする
`makevc`

## ボイスチャンネル以外の人もチームに入れる
`addvc`でvc内のメンバーを追加した後、`add`か`join`でメンバーを追加

## ボイスチャンネルにいるけどチームに入らない人がいる
`addvc`でvc内のメンバーを追加した後、`delete`か`leave`でメンバーを削除


# コマンド一覧

**コマンドの最初には接頭語(初期設定では"!")を付ける必要があります。**<br>
**コマンドの"<"、">"は入力する必要がありません。**

## 基本的なコマンド
- `add <名前>`  
新しいメンバーをBotに登録します。<br>
既に同じ名前が登録されている場合、登録は行われません。<br>
複数の名前を入力する場合、空白で区切ってください。

- `delete <名前>`  
名前が一致したメンバーを、Botから削除します。<br>
複数の名前を入力する場合、空白で区切ってください。

- `clear`  
Botに登録済みのメンバーを全て削除します。

- `list`  
Botに登録済みのメンバーを全て表示します。

- `make`  
Botに登録済みのメンバーでチーム分けを行います。

## ボイスチャンネルを利用するコマンド
- `addvc`  
コマンドの送信者と同じボイスチャンネルに接続中のメンバーを、Botに登録します。

- `makevc`  
コマンドの送信者と同じボイスチャンネルに接続中のメンバーで、チーム分けを行います。<br>
ボイスチャンネルにいるメンバーはBotに登録されます。<br>
ボイスチャンネルにいないメンバーはBotから削除されます。

## 設定
- `tnum <チーム数>`  
チーム数を変更します

- `tsize <人数>`  
1チームの最大人数を設定します

## その他
- `join`(未実装)  
コマンドの送信者自身をBotに登録します。<br>

- `leave`(未実装)  
コマンドの送信者自身をBotから削除します。<br>

- `hello`  
コマンドを送信したチャンネルに"hello"と送信します。
botが起動しているかを確かめることが出来ます。


# 注意事項
- Botを複数のサーバーで同時に使うことは想定していません。
