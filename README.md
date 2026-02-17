A small Anki add-on that removes HTML non-breaking spaces (`&nbsp;`) and replaces them with normal spaces.

![Demonstration showing removing nbsp from Anki card](https://github.com/qais8r/anki-nbsp-remover/blob/main/assets/demo.gif?raw=true)

## Features

- Cleans newly added notes automatically:
  - Hooks into the Add Cards flow.
  - After a note is added, scans every field and replaces `&nbsp;` with a regular space.
- Collection-wide purge command:
  - Adds a Tools menu entry: `Tools -> nbsp Remover -> Purge collection from &nbsp;`.
  - Runs Anki's background find/replace across all notes.
- Optional startup purge:
  - Can run the collection-wide purge automatically when Anki starts.
- Configurable keyboard shortcut:
  - Shortcut for the manual purge action (default: `Ctrl+Alt+P`).
- Optional tooltips:
  - Shows confirmation/status tooltips after cleanup actions.

## Menu Entries

After Anki starts, this add-on creates:

- `Tools -> nbsp Remover -> Purge collection from &nbsp;`
- `Tools -> nbsp Remover -> Options`

It also registers the add-on config action so Options can be opened from Anki's add-on config entry point.

## Notes

- Replacement target is the exact text `&nbsp;` (not regex).
- Replacement value is a normal space (` `).
- Purge runs in the background using Anki operations.
