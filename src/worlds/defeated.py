from typing import Sequence

from common import util
from common.event import EventType, GameEvent
from common.util import now
from worlds.base_scene import BaseScene


class Defeated(BaseScene):
    """Show when player dies."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.created_at_ms: int = now()

    def tick(self, events: Sequence[GameEvent]) -> bool:
        super().tick(events)
        # TODO: clean up, move hardcoded values to configs
        util.display_text(
            self.screen,
            text="Bạn đã chết!!! (You died!)",
            x=200,
            y=200,
            font_size=32,
        )
        util.display_text(
            self.screen,
            text="Sự thật thú vị (Fun Fact):",
            x=200,
            y=400,
            font_size=32,
        )
        util.display_text(
            self.screen,
            text="Có 1 dòng chữ ẩn đấy, bạn tìm ra được không? =)))",
            x=200,
            y=500,
            font_size=32,
        )
        util.display_text(
            self.screen,
            text="Never Gonna Give You Up",
            x=200,
            y=0,
            font_size=5
        )
        now_ms = now()
        if now_ms - self.created_at_ms > 1800:
            util.display_text(self.screen, text="Restarting level ...", x=200, y=300, font_size=32)
        if now_ms - self.created_at_ms > 4100:
            GameEvent(EventType.RESTART_LEVEL).post()
        return True
