from __future__ import annotations

from typing import Optional

from PySide6.QtCore import QSettings

from src.core.app_state import AppState
from src.core.services import DeviceService, ApplyService
class AppUseCases:
    def __init__(self, state: AppState, device_service: DeviceService, apply_service: ApplyService):
        self.state = state
        self.device_service = device_service
        self.apply_service = apply_service

    def refresh_devices(self, settings: QSettings, alert_callback=lambda _x: None):
        self.state.busy = True
        try:
            self.device_service.refresh_devices(settings, alert_callback)
            self.state.canApply = len(self.device_service.manager.devices) > 0
        finally:
            self.state.busy = False

    def apply(self, update_label=lambda _x: None, alert_callback=lambda _x: None):
        self.state.busy = True
        self.state.progress = "Applying changes..."
        try:
            self.apply_service.apply(self._progress_proxy(update_label), self._alert_proxy(alert_callback))
        finally:
            self.state.busy = False

    def reset(self, reset_pages: list, settings: QSettings, update_label=lambda _x: None, alert_callback=lambda _x: None):
        self.state.busy = True
        self.state.progress = "Resetting tweaks..."
        try:
            self.apply_service.reset(reset_pages, settings, self._progress_proxy(update_label), self._alert_proxy(alert_callback))
        finally:
            self.state.busy = False

    def _progress_proxy(self, downstream):
        def inner(text: str):
            self.state.progress = text or ""
            downstream(text)
        return inner

    def _alert_proxy(self, downstream):
        def inner(alert):
            if alert is not None and getattr(alert, "icon", None) is not None:
                if "Error" in alert.title:
                    self.state.lastError = alert.txt
            downstream(alert)
        return inner
