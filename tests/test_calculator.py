import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from calculator import add


def test_add():
    result = add(2, 3)
    assert result == 5
