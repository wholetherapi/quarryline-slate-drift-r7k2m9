from slate_drift.diff import diff_trees


def test_nested_drift():
    left = {"db": {"pool": 10, "host": "a"}}
    right = {"db": {"pool": 20, "host": "a"}}
    entries = diff_trees(left, right)
    assert [entry.path for entry in entries] == ["db.pool"]
