from aqt import mw
from aqt.operations.note import find_and_replace

from .utils import purge_tooltip

TARGET_TEXT = "&nbsp;"


def clean_collection() -> None:
    op = find_and_replace(
                parent=mw,
                note_ids=[],
                search=TARGET_TEXT,
                replacement=" ",
                regex=False,
                field_name=None,
                match_case=True,
            )

    op.success(
                lambda out: purge_tooltip(mw, out.count)
            )
    op.run_in_background()
