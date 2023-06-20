from typing import List

STATE_VERSION_KEY = "version"
STATE_ACTIVE_KEY = "active"
OLD_STATE_ACTIVE_KEY = "bgg-ids"  # TODO: deprecated, remove old key
STATE_TO_ADD_KEY = "to_add"
STATE_TO_DROP_KEY = "to_drop"


class CollectionState:
    """Collection state record."""

    def __init__(
        self,
        active_ids: List[int] = [],
        to_add_ids: List[int] = [],
        to_drop_ids: List[int] = [],
    ):
        self.active_ids = active_ids
        self.to_add_ids = to_add_ids
        self.to_drop_ids = to_drop_ids

    def __bool__(self) -> bool:
        return (
            len(self.active_ids) > 0
            or len(self.to_add_ids) > 0
            or len(self.to_drop_ids) > 0
        )

    def to_dict(self) -> dict:
        return {
            STATE_VERSION_KEY: "v1.0",  # TODO: make this dynamic
            STATE_ACTIVE_KEY: self.active_ids,
            STATE_TO_ADD_KEY: self.to_add_ids,
            STATE_TO_DROP_KEY: self.to_drop_ids,
        }

    @staticmethod
    def from_dict(state_dict: dict):
        # TODO: deprecated - remove old key check
        if OLD_STATE_ACTIVE_KEY in state_dict:
            active_ids = state_dict[OLD_STATE_ACTIVE_KEY]
        else:
            active_ids = state_dict[STATE_ACTIVE_KEY]
        return CollectionState(
            active_ids=active_ids,
            to_add_ids=state_dict[STATE_TO_ADD_KEY],
            to_drop_ids=state_dict[STATE_TO_DROP_KEY],
        )
