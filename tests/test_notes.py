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


def test_export_csv_header():
    n = Notes()
    n.add("a", "b", ["t"])
    assert n.export_csv().splitlines()[0] == "id,title,body,tags"
