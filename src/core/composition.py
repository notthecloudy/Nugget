from __future__ import annotations

from dataclasses import dataclass

from src.core.app_state import AppState
from src.core.services import DeviceService, ApplyService
from src.core.settings_store import SettingsStore
from src.core.tweak_registry import TweakRegistry
from src.core.use_cases import AppUseCases
from src.devicemanagement.device_manager import DeviceManager


@dataclass
class AppContext:
    device_manager: DeviceManager
    app_state: AppState
    tweak_registry: TweakRegistry
    device_service: DeviceService
    apply_service: ApplyService
    settings_store: SettingsStore
    use_cases: AppUseCases


def build_app_context(device_manager: DeviceManager, settings=None) -> AppContext:
    state = AppState()
    tweak_registry = TweakRegistry()
    device_service = DeviceService(device_manager)
    apply_service = ApplyService(device_manager)
    settings_store = SettingsStore(settings) if settings is not None else None
    use_cases = AppUseCases(state=state, device_service=device_service, apply_service=apply_service)
    return AppContext(
        device_manager=device_manager,
        app_state=state,
        tweak_registry=tweak_registry,
        device_service=device_service,
        apply_service=apply_service,
        settings_store=settings_store,
        use_cases=use_cases,
    )
