class Member():
    """
    チームメーカーのメンバー
    """
    def __init__(self, name: str, fixed: bool=False) -> None:
        self.name: str = name
        self.__fixed: bool = False
        self.__priority: int = 0
        if fixed:
            self.fix()
    
    @property
    def priority(self):
        return self.__priority
    
    def fix(self) -> None:
        self.__fixed = True
        self.__priority = 1000
    
    def unfix(self) -> None:
        self.__fixed = False
        self.__priority = 0

    def priority_change(self, x: int) -> None:
        if self.__fixed:
            return
        self.__priority += x
    
    def priority_reset(self) -> None:
        if self.__fixed:
            return
        self.__priority = 0

    def __str__(self) -> str:
        return self.name