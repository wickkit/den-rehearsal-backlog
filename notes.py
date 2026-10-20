"""A tiny in-memory notes store: the rehearsal project den grooms."""
import csv
import io


class Notes:
    def __init__(self):
        self.items = []

    def add(self, title, body="", tags=()):
        if any(not t.strip() for t in tags):
            raise ValueError("tag must not be empty")
        note = {"id": len(self.items) + 1, "title": title, "body": body, "tags": [t.lower() for t in tags]}
        self.items.append(note)
        return note

    def get(self, note_id):
        for n in self.items:
            if n["id"] == note_id:
                return n
        return None

    def search(self, text):
        text = text.lower()
        return [n for n in self.items if text in n["title"].lower() or text in n["body"].lower()]

    def with_tag(self, tag):
        return [n for n in self.items if tag.lower() in n["tags"]]

    def rename_tag(self, old, new):
        old, new = old.lower(), new.lower()
        for n in self.items:
            n["tags"] = [new if t == old else t for t in n["tags"]]

    def untag(self, note_id, tag):
        note = self.get(note_id)
        if note is not None:
            note["tags"] = [t for t in note["tags"] if t != tag.lower()]

    def export_csv(self):
        out = io.StringIO()
        w = csv.writer(out)
        w.writerow(["id", "title", "body", "tags"])
        for n in self.items:
            w.writerow([n["id"], n["title"], n["body"], " ".join(n["tags"])])
        return out.getvalue()
