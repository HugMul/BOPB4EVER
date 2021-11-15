# tests/test_lib.py
from BOPB4EVER.lib import try_me


def test_length_of_try_me():
    assert len(try_me()) != 0
