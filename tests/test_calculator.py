import sys
import os
from calculator import add

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


def test_add():
    result = add(2, 3)
    assert result == 6  # nosec
