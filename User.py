import random


class User:
    id: str

    def __init__(self, id: str):
        self.id = id

    def __repr__(self):
        return f"User: id: {self.id}"


class Computer(User):

    def __init__(self, id: str):
        super().__init__(id=id)

    def __repr__(self):
        return f"Computer: id: {self.id}"

    def select_index_from_list(self, list: list, quantity: int) -> list[int]:
        _output = []
        while len(_output) < quantity and list:
            _number = random.randint(0, len(list) - 1)
            _output.append(_number) if _number not in _output else False
        _output.sort(reverse=True)
        return _output
