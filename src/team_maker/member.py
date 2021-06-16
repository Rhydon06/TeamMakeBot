
class Member():
    """
    チームメーカーのメンバー
    """
    def __init__(self, id: int, fixed: bool=False) -> None:
        self.id: int = id
        self.fixed: bool = fixed
        self.priority: int = 0