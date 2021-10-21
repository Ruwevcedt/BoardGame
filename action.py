class Action:
    name: str
    condition_procedure: list[str] or None
    condition_card_letter: list[str]

    def __init__(self, name, function,
                 condition_procedure: list[str] or None = None,
                 condition_card_letter: list[str] or None = None):
        self.name = name
        self.condition_procedure = condition_procedure
        self.condition_card_letter = condition_card_letter

draw = Action('draw', [], [])


ALL_ACTION = [

]