from typing import Dict, List, Tuple
import random
from .member import Member

class TeamMaker():
    """
    チームメーカー
    """
    def __init__(self) -> None:
        # チーム作成時に使うメンバー
        self.__members: List[Member] = []
        
        # 完成済みチーム
        self.teams: List[List[Member]] = []
        # チーム分け時に余ったメンバー
        self.remainder: List[Member] = []

        # チームの数
        self.team_num: int = 2
        # 1チームの最大人数
        self.team_size: int = 5

    def add_member(self, name: str) -> None:
        """
        チームメーカーにメンバーを追加する
        既に同じ名前のメンバーが追加されている場合ValueErrorを発生させる
        """
        # 登録する名前と同じ名前のメンバーが既に存在する場合、登録をしない
        for member in self.__members:
            if member.name == name:
                raise ValueError("同じ名前のメンバーが既に追加されています。")

        # メンバーを追加
        self.__members.append(Member(name))
    
    def delete_member(self, name: str) -> None:
        """
        指定した名前のメンバーを削除する
        指定した名前が無い場合ValueErrorを発生させる
        """
        # 指定した名前のメンバーを削除
        for member in self.__members:
            if member.name == name:
                self.__members.remove(member)
                return

        else:
            # 指定した名前が見つからなければValueErrorを発生させる
            raise ValueError("指定した名前のメンバーは追加されていません。")
    
    def clear_member(self) -> None:
        """
        全てのメンバーを削除
        """
        self.__members.clear()

    def make_team(self) -> Tuple[List[List[Member]], List[Member]]:
        """
        追加済みのメンバーからチームを作成する
        メンバーが少ない場合、メンバーは全てのチームに均等に振り分けられる
        メンバーが多い場合、余りとして分けられる
        """
        # 1.チームに振り分けるメンバーと余りになるメンバーを決める
        # 2.各チームに振り分ける
        # 3.優先度の変更

        # 1.チームに振り分けるメンバーと余りのメンバーを分ける

        # チームに入ることができる人数（チーム数*1チームの上限）
        limit = self.team_num*self.team_size
        shuffled_members = random.sample(self.__members, len(self.__members))
        # 優先度順に並び変える　同じ優先度のメンバーの並びはランダムのまま
        shuffled_members.sort(key=lambda member: member.priority, reverse=True)

        # この後チームに振り分けるメンバー
        team_member = shuffled_members[:limit]
        # 余り
        self.remainder = sorted(shuffled_members[limit:], key=lambda member: member.name)


        # 2.チーム分けを行う
        # チーム数が2、チームの人数が5の場合
        # [A, B, C, D, E, F, G, H, I, J] -> [[A, C, E, G, I],[B, D, F, H, J]]
        teams = []
        for i in range(self.team_num):
            team = team_member[i::self.team_num]
            team = sorted(team, key=lambda member: member.name)
            if team:
                teams.append(team)
        self.teams = teams

        # 3.優先度の変更
        for member in self.remainder:
            member.priority_change(1)
        for team in self.teams:
            for member in team:
                member.priority_reset()

        return self.teams, self.remainder
    

    def fix(self, name) -> None:
        """
        指定した名前のメンバーを固定する
        指定した名前が無い場合ValueErrorを発生させる
        """
        # 指定した名前のメンバーを固定
        for member in self.__members:
            if member.name == name:
                member.fix()
                return

        else:
            # 指定した名前が見つからなければValueErrorを発生させる
            raise ValueError("指定した名前のメンバーは追加されていません。")
    

    def unfix(self, name) -> None:
        """
        指定した名前のメンバーの固定を解除する
        指定した名前が無い場合ValueErrorを発生させる
        """
        # 指定した名前のメンバーの固定を解除
        for member in self.__members:
            if member.name == name:
                member.unfix()
                return

        else:
            # 指定した名前が見つからなければValueErrorを発生させる
            raise ValueError("指定した名前のメンバーは追加されていません。")