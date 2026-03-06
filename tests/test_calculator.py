import sys
import os
from calculator import add

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


def test_add():
    result = add(2, 3)
    assert result == 5
