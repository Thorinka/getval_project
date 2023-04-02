import pytest

from utils import dicts


@pytest.fixture
def coll():
    return {"vcs": "mercurial"}


def test_get_val(coll):
    assert dicts.get_val(coll, "vcs") == "mercurial"
    assert dicts.get_val(coll, "vcs", "git") == "mercurial"
    assert dicts.get_val({}, "vcs", "git") == "git"
    assert dicts.get_val({}, "vcs", "bazaar") == "bazaar"
