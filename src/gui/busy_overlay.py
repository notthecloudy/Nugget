from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class BusyOverlay(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 120); border-radius: 8px;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.addStretch()
        self.label = QLabel("Working...", self)
        self.label.setStyleSheet("font-size: 15px; font-weight: 600; color: #FFFFFF;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        layout.addStretch()
        self.hide()

    def sync_geometry(self):
        self.setGeometry(self.parent().rect())

    def set_message(self, message: str):
        self.label.setText(message or "Working...")
