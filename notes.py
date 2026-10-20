"""A tiny in-memory notes store: the rehearsal project den grooms."""
import csv
import io


class Notes:
    def __init__(self):
        self.items = []

    def add(self, title, body="", tags=()):
        note = {"id": len(self.items) + 1, "title": title, "body": body, "tags": list(tags)}
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
        return [n for n in self.items if tag in n["tags"]]

    def export_csv(self):
        out = io.StringIO()
        w = csv.writer(out)
        w.writerow(["id", "title", "body", "tags"])
        for n in self.items:
            w.writerow([n["id"], n["title"], n["body"], " ".join(n["tags"])])
        return out.getvalue()
