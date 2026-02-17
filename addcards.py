from aqt import mw
from anki.notes import Note
from aqt.addcards import AddCards
from aqt.gui_hooks import (
    add_cards_did_init,
    add_cards_did_add_note,
)

from .utils import editing_tooltip

TARGET_TEXT = "&nbsp;"
REPLACEMENT_TEXT = " "

addcards: AddCards = None

def store_addcards(instance: AddCards) -> None:
    global addcards
    addcards = instance


def on_add(note: Note) -> None:
    count = 0
    for (name, value) in note.items():
        replacements = value.count(TARGET_TEXT)
        if replacements > 0:
            count += replacements
            note[name] = value.replace(TARGET_TEXT, REPLACEMENT_TEXT)

    if count > 0:
        mw.col.update_note(note)
        editing_tooltip(addcards, count)


def init_addcards() -> None:
    add_cards_did_init.append(store_addcards)
    add_cards_did_add_note.append(on_add)
