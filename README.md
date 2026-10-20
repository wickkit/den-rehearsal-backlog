# den-rehearsal-backlog

A toy notes library with an old, messy backlog. It exists so den can practise grooming a backlog it didn't write.

## Notes

- `add(title, body="", tags=())`: a new note; tags are stored lower-case, an empty tag raises `ValueError`.
- `get(note_id)`: the note with that id, or `None`.
- `search(text)`: notes whose title or body contains `text`, any case.
- `with_tag(tag)`: notes carrying `tag`, any case.
- `rename_tag(old, new)`: renames a tag on every note.
- `untag(note_id, tag)`: drops a tag from one note.
- `tag_counts()`: `{tag: number of notes}`.
- `export_csv()`: every note as CSV (`id,title,body,tags`).

Tests: `pip install pytest && python -m pytest -q`.
