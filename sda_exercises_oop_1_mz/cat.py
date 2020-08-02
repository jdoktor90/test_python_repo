class Cat:

    def __init__(self, name: str):
        self.name = name
        self.eat = 0

    def make_sound(self) -> str:
        return f"{self.name} miau"

    def eat_mause(self) -> None:
        self.eat += 1
        print(f"{self.name} zjadł {self.eat} myszy")