from __future__ import annotations

from typing import Callable, Optional

from PySide6.QtCore import QSettings

from src.devicemanagement.device_manager import DeviceManager


class DeviceService:
    def __init__(self, manager: DeviceManager):
        self.manager = manager

    def refresh_devices(self, settings: QSettings, alert_callback: Callable):
        self.manager.get_devices(settings, alert_callback)

    def select_device(self, index: Optional[int]):
        self.manager.set_current_device(index=index)


class ApplyService:
    def __init__(self, manager: DeviceManager):
        self.manager = manager

    def apply(self, update_label: Callable, alert_callback: Callable):
        self.manager.apply_changes(update_label, alert_callback)

    def reset(self, reset_pages, settings: QSettings, update_label: Callable, alert_callback: Callable):
        self.manager.reset_tweaks(reset_pages, settings, update_label, alert_callback)
