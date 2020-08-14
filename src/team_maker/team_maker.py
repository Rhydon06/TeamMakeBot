import random
from .member import Member

class TeamMaker():
    """
    チームメーカー
    """
    def __init__(self) -> None:
        # チーム作成時に使うメンバー
        self.members = []
        
        # 完成済みチーム
        self.teams = []
        # チーム分け時に余ったメンバー
        self.remainder = []

        # チームの数
        self.team_num = 2
        # 1チームの最大人数
        self.team_size = 5

    def add_member(self, name: str) -> None:
        """
        チームメーカーにメンバーを追加する
        既に同じ名前のメンバーが追加されている場合ValueErrorを発生させる
        """
        # 登録する名前と同じ名前のメンバーが既に存在する場合、登録をしない
        for member in self.members:
            if member.name == name:
                raise ValueError("同じ名前のメンバーが既に追加されています。")

        # メンバーを追加
        self.members.append(Member(name))
    
    def delete_member(self, name: str) -> None:
        """
        指定した名前のメンバーを削除する
        指定した名前が無い場合ValueErrorを発生させる
        """
        # 指定した名前のメンバーを削除
        for member in self.members:
            if member.name == name:
                self.members.remove(member)
                return

        else:
            # 指定した名前が見つからなければValueErrorを発生させる
            raise ValueError("指定した名前のメンバーは追加されていません。")
    
    def clear_member(self) -> None:
        """
        全てのメンバーを削除
        """
        self.members.clear()

    def make_team(self) -> None:
        """
        追加済みのメンバーからチームを作成する
        メンバーが少ない場合、メンバーは全てのチームに均等に振り分けられる
        メンバーが多い場合、余りとして分けられる
        """
        # 1.チームに振り分けるメンバーと余りになるメンバーを決める
        # 2.各チームに振り分ける


        # 1.チームに振り分けるメンバーと余りのメンバーを分ける

        # チームに入ることができる人数（チーム数*1チームの上限）
        limit = self.team_num*self.team_size
        shuffled_members = random.sample(self.members, len(self.members))

        # この後チームに振り分けるメンバー
        team_member = shuffled_members[:limit]
        # 余り
        self.remainder = shuffled_members[limit:]


        # 2.チーム分けを行う
        # チーム数が2、チームの人数が5の場合
        # [A, B, C, D, E, F, G, H, I, J] -> [[A, C, E, G, I],[B, D, F, H, J]]
        teams = []
        for i in range(self.team_num):
            team = team_member[i::self.team_num]
            team = sorted(team, key=lambda x: x.name)
            teams.append(team)
        
        self.teams = teams
