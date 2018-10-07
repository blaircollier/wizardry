

class Character(object):
    def __init__(self):
        self._age = 0.
        self._strength = 0.
        self._intelligence = 0.
        self._luck = 0.
        self._inventory = []
        self._weapon = None
        self._armor = None

class Fighter(Character):
    def __init__(self):
        super(Fighter, self).__init__()

class Priest(Character):
    def __init__(self):
        super(Priest, self).__init__()

class Dwarf(Character):
    def __init__(self):
        super(Dwarf, self).__init__()
