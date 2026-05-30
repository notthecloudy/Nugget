from __future__ import annotations

from PySide6.QtCore import QObject, Signal, QUrl, Property, Slot
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtWidgets import QWidget

from src.core.app_state import AppState
from src.controllers.files_handler import get_bundle_files


class ShellBridge(QObject):
    navigateRequested = Signal(int)

    def __init__(self, state: AppState):
        super().__init__()
        self.state = state
        self.state.progressChanged.connect(self.progressChanged)
        self.state.busyChanged.connect(self.busyChanged)

    progressChanged = Signal(str)
    busyChanged = Signal(bool)

    @Property(str, notify=progressChanged)
    def progress(self):
        return self.state.progress

    @Property(bool, notify=busyChanged)
    def busy(self):
        return self.state.busy

    @Slot(int)
    def navigate(self, page_id: int):
        self.navigateRequested.emit(page_id)


class QmlShell:
    def __init__(self, parent: QWidget, app_state: AppState):
        self.bridge = ShellBridge(app_state)
        self.widget = QQuickWidget(parent)
        self.widget.setClearColor(parent.palette().window().color())
        self.widget.rootContext().setContextProperty("shellBridge", self.bridge)

        qml_path = get_bundle_files("src/qml/Shell.qml")
        self.widget.setSource(QUrl.fromLocalFile(qml_path))
        self.widget.hide()
