from app_logic.inflect_words import get_plurals

plurals = get_plurals("this is the house, this is the hill")
assert plurals.pop("this") == "these"
for k, v in plurals.items():
    assert v == f"{k}s"