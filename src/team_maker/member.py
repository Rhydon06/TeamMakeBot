class Member():
    """
    チームメーカーのメンバー
    """
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.priority: int = 1

    def __str__(self) -> str:
        return self.name