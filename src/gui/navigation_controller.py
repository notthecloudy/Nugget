from __future__ import annotations

from PySide6.QtCore import QEasingCurve, QPropertyAnimation
from PySide6.QtWidgets import QGraphicsOpacityEffect, QStackedWidget


class NavigationController:
    def __init__(self, stacked_widget: QStackedWidget):
        self.stacked_widget = stacked_widget
        self._effect = QGraphicsOpacityEffect(stacked_widget)
        self.stacked_widget.setGraphicsEffect(self._effect)
        self._effect.setOpacity(1.0)

    def navigate(self, page_index: int):
        fade_out = QPropertyAnimation(self._effect, b"opacity")
        fade_out.setDuration(130)
        fade_out.setStartValue(1.0)
        fade_out.setEndValue(0.25)
        fade_out.setEasingCurve(QEasingCurve.Type.InOutQuad)

        fade_in = QPropertyAnimation(self._effect, b"opacity")
        fade_in.setDuration(180)
        fade_in.setStartValue(0.25)
        fade_in.setEndValue(1.0)
        fade_in.setEasingCurve(QEasingCurve.Type.InOutQuad)

        def switch_page():
            self.stacked_widget.setCurrentIndex(page_index)
            fade_in.start()

        fade_out.finished.connect(switch_page)
        fade_out.start()
