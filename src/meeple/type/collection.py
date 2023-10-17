from typing import List

from meeple.type.collection_data import CollectionData
from meeple.type.collection_state import CollectionState
from meeple.type.item import Item
from meeple.util.api_util import BOARDGAME_TYPE, EXPANSION_TYPE


class Collection:
    """Collection of board game and expansion items."""

    def __init__(
        self,
        name: str,
        state: CollectionState = CollectionState(),
        data: CollectionData = CollectionData(),
    ):
        self.name = name
        self.state = state
        self.data = data

    def get_board_games(self) -> List[Item]:
        # get latest stored board games for this collection
        return [item for item in self.data.items if item.type == BOARDGAME_TYPE]

    def get_expansions(self) -> List[Item]:
        # get latest stored expansions for this collection
        return [item for item in self.data.items if item.type == EXPANSION_TYPE]

    def is_pending_updates(self) -> bool:
        return (
            len(self.state.to_add_ids) > 0
            or len(self.state.to_drop_ids) > 0
            or (len(self.state.active_ids) != len(self.data.items))
        )

    def fmt_name(self, styled: bool = True, state: bool = False) -> str:
        fmt_name = self.name
        if styled:
            fmt_name = f"[u magenta]{self.name}[/u magenta]"
        if state and self.is_pending_updates():
            return f"{fmt_name} ([red]*[/red])"
        return fmt_name
