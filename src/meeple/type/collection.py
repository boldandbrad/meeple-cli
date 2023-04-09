class Collection:
    """Collection of boardgames and expansions."""

    def __init__(self, name, boardgames, expansions, last_updated):
        self.name = name
        self.boardgames = boardgames
        self.expansions = expansions
        self.last_updated = last_updated
