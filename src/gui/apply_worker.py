from PySide6.QtCore import Signal, QThread, QSettings
from PySide6.QtWidgets import QMessageBox
from typing import Optional

# Global Vars
sudo_pwd = None # reset this variable whenever it is used
sudo_action_complete = False
def get_sudo_pwd() -> Optional[str]:
    pre_reset = sudo_pwd
    set_sudo_pwd(None)
    set_sudo_complete(False)
    return pre_reset
def get_sudo_complete() -> bool:
    return sudo_action_complete
def set_sudo_complete(isComplete: bool):
    global sudo_action_complete
    sudo_action_complete = isComplete
def set_sudo_pwd(pwd: Optional[str]):
    global sudo_pwd
    sudo_pwd = pwd

class ApplyAlertMessage:
    def __init__(self, txt: str, title: str = "Error!", icon = QMessageBox.Critical, detailed_txt: str = None):
        self.txt = txt
        self.title = title
        self.icon = icon
        self.detailed_txt = detailed_txt

class ApplyThread(QThread):
    progress = Signal(str)
    alert = Signal(ApplyAlertMessage)

    def update_label(self, txt: str):
        if txt == 'sudo_pwd':
            # hacky workaround
            self.alert.emit(None)
        else:
            self.progress.emit(txt)
    def alert_window(self, msg: ApplyAlertMessage):
        self.alert.emit(msg)
    
    def __init__(self, manager=None, settings: QSettings = None, reset_pages: Optional[list] = None, use_cases=None, app_state=None):
        super().__init__()
        self.manager = manager
        self.settings = settings
        self.reset_pages = reset_pages
        self.use_cases = use_cases
        self.app_state = app_state

    def do_work(self):
        if self.use_cases is not None:
            if self.reset_pages is None:
                self.use_cases.apply(self.update_label, self.alert_window)
            else:
                self.use_cases.reset(self.reset_pages, self.settings, self.update_label, self.alert_window)
            return
        if self.reset_pages == None:
            # applying tweaks
            self.manager.apply_changes(self.update_label, self.alert_window)
        else:
            # resetting tweaks
            self.manager.reset_tweaks(self.reset_pages, self.settings, self.update_label, self.alert_window)

    def run(self):
        self.do_work()

class RefreshDevicesThread(QThread):
    alert = Signal(ApplyAlertMessage)

    def alert_window(self, msg: ApplyAlertMessage):
        self.alert.emit(msg)

    def __init__(self, manager=None, settings=None, use_cases=None):
        super().__init__()
        self.manager = manager
        self.settings = settings
        self.use_cases = use_cases

    def do_work(self):
        if self.use_cases is not None:
            self.use_cases.refresh_devices(self.settings, self.alert_window)
        else:
            self.manager.get_devices(self.settings, self.alert_window)

    def run(self):
        self.do_work()