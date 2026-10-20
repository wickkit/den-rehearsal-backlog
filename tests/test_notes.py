import pytest
from notes import Notes


def test_add_and_get():
    n = Notes()
    a = n.add("groceries", "milk")
    assert n.get(a["id"])["body"] == "milk"


def test_search_title_and_body():
    n = Notes()
    n.add("Groceries", "milk")
    n.add("work", "call about milk")
    assert len(n.search("MILK")) == 2


def test_with_tag():
    n = Notes()
    n.add("a", tags=["home"])
    n.add("b", tags=["work"])
    assert [x["title"] for x in n.with_tag("home")] == ["a"]


def test_rename_tag():
    n = Notes()
    n.add("a", tags=["home"])
    n.add("b", tags=["home", "work"])
    n.add("c", tags=["work"])
    n.rename_tag("home", "house")
    assert [x["title"] for x in n.with_tag("house")] == ["a", "b"]
    assert n.with_tag("home") == []


def test_tag_case_folded():
    n = Notes()
    n.add("a", tags=["Home"])
    n.add("b", tags=["home"])
    assert n.get(1)["tags"] == ["home"]
    assert [x["title"] for x in n.with_tag("HOME")] == ["a", "b"]


def test_untag_only_that_note():
    n = Notes()
    n.add("a", tags=["home"])
    n.add("b", tags=["home"])
    n.untag(1, "HOME")
    assert n.get(1)["tags"] == []
    assert [x["title"] for x in n.with_tag("home")] == ["b"]


def test_empty_tag_rejected():
    n = Notes()
    for bad in ("", "   "):
        with pytest.raises(ValueError):
            n.add("a", tags=[bad])
    assert n.items == []


def test_tag_counts():
    n = Notes()
    n.add("a", tags=["home", "work"])
    n.add("b", tags=["home"])
    n.add("c", tags=["Home"])
    assert n.tag_counts() == {"home": 3, "work": 1}


def test_export_csv_header():
    n = Notes()
    n.add("a", "b", ["t"])
    assert n.export_csv().splitlines()[0] == "id,title,body,tags"
