from action import Action, ALL_ACTION

class Phase:
    name: str
    available_action: list[Action]

    def __init__(self, name: str, available_action:list[Action]):
        self.name = name
        self.available_action = available_action


class Season:
    name: str
    procedures: list[Phase]

    def __init__(self, name: str, procedure: list[Phase]):
        self.name = name
        self.procedure = procedure


class Year:
    open: Season
    administration: Season
    diplomacy: Season
    draft: Season
    war: Season
    end: Season

    def __init__(self):
        self.open = Season()

