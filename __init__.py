from aqt import gui_hooks, mw
from aqt.qt import QAction, QKeySequence, QMenu, qconnect

from .addcards import init_addcards
from .collection import clean_collection
from .config_dialog import show_config_dialog

DEFAULT_PURGE_SHORTCUT = "Ctrl+Alt+P"
purge_action = None  # type: QAction


def _config():
    return mw.addonManager.getConfig(__name__) or {}


def update_purge_shortcut() -> None:
    if purge_action is None:
        return

    config = _config()
    shortcut = config.get("purge_shortcut", DEFAULT_PURGE_SHORTCUT)
    purge_action.setShortcut(QKeySequence(shortcut))


def show_options() -> None:
    show_config_dialog(on_saved=update_purge_shortcut)


def init_anki_home_menu() -> None:
    global purge_action

    remover_menu = QMenu("nbsp Remover", mw)

    purge_action = QAction("Purge collection from &nbsp;", mw)
    qconnect(purge_action.triggered, clean_collection)
    update_purge_shortcut()
    remover_menu.addAction(purge_action)

    options_action = QAction("Options", mw)
    qconnect(options_action.triggered, show_options)
    remover_menu.addAction(options_action)

    mw.form.menuTools.addMenu(remover_menu)
    mw.addonManager.setConfigAction(__name__, show_options)


def run_startup_clean_collection() -> None:
    config = _config()
    if config.get("auto_run_startup", False):
        clean_collection()


def run_start_up(*args, **kwargs) -> None:
    init_anki_home_menu()
    run_startup_clean_collection()


init_addcards()
gui_hooks.main_window_did_init.append(run_start_up)
