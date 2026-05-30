from __future__ import annotations

from src.tweaks.tweaks import tweaks


class TweakRegistry:
    """Thin indirection around the global tweaks dict."""

    def all(self) -> dict:
        return tweaks

    def get(self, key):
        return tweaks.get(key)

    def has(self, key) -> bool:
        return key in tweaks
