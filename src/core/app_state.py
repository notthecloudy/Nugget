from __future__ import annotations

from PySide6.QtCore import QObject, Signal, Property


class AppState(QObject):
    busyChanged = Signal(bool)
    progressChanged = Signal(str)
    currentPageChanged = Signal(int)
    selectedDeviceChanged = Signal(str)
    lastErrorChanged = Signal(str)
    canApplyChanged = Signal(bool)

    def __init__(self):
        super().__init__()
        self._busy = False
        self._progress = ""
        self._current_page = 0
        self._selected_device = ""
        self._last_error = ""
        self._can_apply = False

    def get_busy(self) -> bool:
        return self._busy

    def set_busy(self, value: bool):
        if self._busy != value:
            self._busy = value
            self.busyChanged.emit(value)

    busy = Property(bool, get_busy, set_busy, notify=busyChanged)

    def get_progress(self) -> str:
        return self._progress

    def set_progress(self, value: str):
        if self._progress != value:
            self._progress = value
            self.progressChanged.emit(value)

    progress = Property(str, get_progress, set_progress, notify=progressChanged)

    def get_current_page(self) -> int:
        return self._current_page

    def set_current_page(self, value: int):
        if self._current_page != value:
            self._current_page = value
            self.currentPageChanged.emit(value)

    currentPage = Property(int, get_current_page, set_current_page, notify=currentPageChanged)

    def get_selected_device(self) -> str:
        return self._selected_device

    def set_selected_device(self, value: str):
        if self._selected_device != value:
            self._selected_device = value
            self.selectedDeviceChanged.emit(value)

    selectedDevice = Property(str, get_selected_device, set_selected_device, notify=selectedDeviceChanged)

    def get_last_error(self) -> str:
        return self._last_error

    def set_last_error(self, value: str):
        if self._last_error != value:
            self._last_error = value
            self.lastErrorChanged.emit(value)

    lastError = Property(str, get_last_error, set_last_error, notify=lastErrorChanged)

    def get_can_apply(self) -> bool:
        return self._can_apply

    def set_can_apply(self, value: bool):
        if self._can_apply != value:
            self._can_apply = value
            self.canApplyChanged.emit(value)

    canApply = Property(bool, get_can_apply, set_can_apply, notify=canApplyChanged)
