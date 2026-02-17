# nbsp; remover

Install the Anki addon from [AnkiWeb](https://ankiweb.net/shared/info/1454160524).

## Description

A small Anki add-on that removes HTML non-breaking spaces (`&nbsp;`) and replaces them with normal spaces.

![Demonstration showing removing nbsp from Anki card](https://github.com/qais8r/anki-nbsp-remover/blob/main/assets/demo.gif?raw=true)

## Features

- Cleans newly added notes automatically by hooking into Add Cards and replacing `&nbsp;` with a regular space in every field after a note is added.
- Adds a collection-wide purge command at `Tools -> nbsp Remover -> Purge collection from &nbsp;` that runs Anki's background find/replace across all notes.
- Supports optional startup purge to run the collection-wide cleanup automatically when Anki starts.
- Supports a configurable keyboard shortcut for manual purge (default: `Ctrl+Alt+P`).
- Supports optional tooltips that show confirmation/status after cleanup actions.

## Menu Entries

After Anki starts, this add-on creates:

- `Tools -> nbsp Remover -> Purge collection from &nbsp;`
- `Tools -> nbsp Remover -> Options`

It also registers the add-on config action so Options can be opened from Anki's add-on config entry point.

## Notes

- Replacement target is the exact text `&nbsp;` (not regex).
- Replacement value is a normal space (` `).
- Purge runs in the background using Anki operations.
