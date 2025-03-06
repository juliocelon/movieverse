from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Julio", "Celon") == "Celon;Julio"

def test_extract_family_name():
    assert extract_family_name("Celon; Julio") == "Celon"

def test_extract_given_name():
    assert extract_given_name("Celon; Julio") == "Julio"

pytest.main(["-v", "--tb=line", "-rN", __file__])