from meeple.util.api_util import BOARDGAME_TYPE, EXPANSION_TYPE


class Collection:
    """Collection of board game and expansion items."""

    def __init__(self, name, items, last_updated):
        self.name = name
        self.items = items
        self.last_updated = last_updated

    def get_board_games(self):
        return [item for item in self.items if item.type == BOARDGAME_TYPE]

    def get_expansions(self):
        return [item for item in self.items if item.type == EXPANSION_TYPE]
