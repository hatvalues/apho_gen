"""App Tests"""
from app_logic.inflect_words import get_plurals

def test_get_plurals():
    """Test for get_plurals function"""
    plurals = get_plurals("this is the house, this is the hill")
    assert plurals.pop("this") == "these"
    for k, v in plurals.items():
        assert v == f"{k}s"
