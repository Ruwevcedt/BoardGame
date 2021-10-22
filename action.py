from location import Nature, Nation


class _Action:
    name: str
    condition_procedure: list[str] or None
    condition_card: list[str]

    def __init__(self,
                 function,
                 name: str,
                 condition_procedure: list[str] or None = None,
                 condition_card: list[str] or None = None):
        self.function = function
        self.name = name
        self.condition_procedure = condition_procedure
        self.condition_card = condition_card

    def __call__(self, current_phase, current_card):
        if current_phase in self.condition_procedure and current_card in self.condition_card:
            return self.function


def Action(name, condition_procedure, condition_card, current_phase=None, current_card=None, function=None):
    if function and current_phase and current_card:
        return _Action(current_phase, current_card)
    else:
        def wrapper(function, name, condition_procedure, condition_card):
            return _Action(function, name, condition_procedure, condition_card)
        return wrapper()


@Action('draw', condition_procedure=['open_draw'], condition_card=['Q'])
def draw(nature: Nature, nation: Nation, number: int):
    card = nature.deck_draw(number)
    nation.castle.hands.content.append(card)
    nation.castle.initiate_observability()
