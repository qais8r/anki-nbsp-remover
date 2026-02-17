from aqt import mw
from aqt.utils import tooltip

ADDON_MODULE = __name__.split(".")[0]
ASCII_ART = "! ̿̿ ̿̿ ̿̿ ̿'̿'\\̵͇̿̿\\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿"
QUIET_ART = "(▀̿Ĺ̯▀̿ ̿)"


def tooltips_enabled() -> bool:
    config = mw.addonManager.getConfig(ADDON_MODULE) or {}
    return config.get("show_tooltip", True)


def purge_tooltip(parent, count) -> None:
    if not tooltips_enabled():
        return

    notes = "note" if count == 1 else "notes"
    found = f"{count} {notes} purged from &amp;nbsp;<div>{ASCII_ART}</div>"
    not_found = f"{count} {notes} updated.<div>&amp;nbsp; are quiet today...\n{QUIET_ART}</div>"
    tooltip(found if count > 0 else not_found, parent=parent)


def editing_tooltip(parent, count) -> None:
    if not tooltips_enabled() or count <= 0:
        return

    tooltip(
        f"Eliminated {count} &amp;nbsp;<div>{ASCII_ART}</div>",
        parent=parent,
    )
