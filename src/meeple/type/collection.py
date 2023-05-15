class Collection:
    """Collection of board game and expansion items."""

    def __init__(self, name, board_games, expansions, last_updated):
        self.name = name
        self.board_games = board_games
        self.expansions = expansions
        self.last_updated = last_updated
