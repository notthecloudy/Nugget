from __future__ import annotations

from PySide6.QtCore import QSettings


class SettingsStore:
    def __init__(self, settings: QSettings):
        self.settings = settings

    def get_bool(self, key: str, default: bool = False) -> bool:
        return self.settings.value(key, default, type=bool)

    def get_str(self, key: str, default: str = "") -> str:
        return self.settings.value(key, default, type=str)

    def get_int(self, key: str, default: int = 0) -> int:
        return self.settings.value(key, default, type=int)

    def set_value(self, key: str, value):
        self.settings.setValue(key, value)
