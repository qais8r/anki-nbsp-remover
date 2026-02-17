from typing import Callable, Optional

from aqt import mw
from aqt.qt import (
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QKeySequence,
    QKeySequenceEdit,
    QVBoxLayout,
)

ADDON_MODULE = __name__.split(".")[0]
DEFAULT_PURGE_SHORTCUT = "Ctrl+Alt+P"


class ConfigDialog(QDialog):
    def __init__(self, parent=None, on_saved: Optional[Callable[[], None]] = None):
        super().__init__(parent)
        self._on_saved = on_saved

        config = mw.addonManager.getConfig(ADDON_MODULE) or {}

        self.setWindowTitle("nbsp Remover Options")
        self.setMinimumWidth(380)

        self.show_tooltip = QCheckBox("Show tooltips")
        self.show_tooltip.setChecked(config.get("show_tooltip", True))

        self.auto_run_startup = QCheckBox("Run purge at startup")
        self.auto_run_startup.setChecked(config.get("auto_run_startup", False))

        self.purge_shortcut = QKeySequenceEdit(
            QKeySequence(config.get("purge_shortcut", DEFAULT_PURGE_SHORTCUT))
        )

        form = QFormLayout()
        form.addRow("", self.show_tooltip)
        form.addRow("", self.auto_run_startup)
        form.addRow("Purge shortcut", self.purge_shortcut)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save
            | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.save_config)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(buttons)
        self.setLayout(layout)

    def save_config(self) -> None:
        config = mw.addonManager.getConfig(ADDON_MODULE) or {}

        shortcut = self.purge_shortcut.keySequence().toString()
        if not shortcut:
            shortcut = DEFAULT_PURGE_SHORTCUT

        for legacy_key in (
            "search_query",
            "is_regex",
            "is_change_log",
            "last_clean_collection_run",
        ):
            config.pop(legacy_key, None)

        config["show_tooltip"] = self.show_tooltip.isChecked()
        config["auto_run_startup"] = self.auto_run_startup.isChecked()
        config["purge_shortcut"] = shortcut

        mw.addonManager.writeConfig(ADDON_MODULE, config)

        if callable(self._on_saved):
            self._on_saved()

        self.accept()


def show_config_dialog(on_saved: Optional[Callable[[], None]] = None) -> None:
    dialog = ConfigDialog(mw, on_saved=on_saved)
    dialog.exec() if hasattr(dialog, "exec") else dialog.exec_()
