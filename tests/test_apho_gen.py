"""Tests for apho gen"""
from app_logic.apho_gen import get_apho_for_name, partials

def test_get_apho():
    name = "Daniel"
    apho = get_apho_for_name("Daniel")
    assert name in apho
    assert any(p in apho for p in partials)