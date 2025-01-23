from address import extract_city, extract_state, extract_zipcode
import pytest
 
def test_extract_city():
    """Test the extract_city function with various address formats."""
    # Simple addresses
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("1600 Pennsylvania Ave NW, Washington, DC 20500") == "Washington"
 
    # Edge case: address with extra spaces
    assert extract_city("1234 Elm St,  Salt Lake City , UT 84111") == "Salt Lake City"
 
def test_extract_state():
    """Test the extract_state function with various address formats."""
    # Simple addresses
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("1600 Pennsylvania Ave NW, Washington, DC 20500") == "DC"
 
    # Edge case: address with extra spaces
    assert extract_state("1234 Elm St, Salt Lake City,  UT 84111") == "UT"
 
def test_extract_zipcode():
    """Test the extract_zipcode function with various address formats."""
    # Simple addresses
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("1600 Pennsylvania Ave NW, Washington, DC 20500") == "20500"
 
    # Edge case: address with extra spaces
    assert extract_zipcode("1234 Elm St, Salt Lake City, UT 84111") == "84111"
 
def extract_city(full_address):
    """Extract and return the name of a city from
    a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the city name
    """
    full_address = full_address.strip()
    last_comma_index = full_address.rindex(",")
    mid_comma_index = full_address.rindex(",", 0, last_comma_index)
    city = full_address[mid_comma_index + 1 : last_comma_index]
    city = city.strip()
    return city
 
 
def extract_state(full_address):
    """Extract and return the two letter abbreviation for
    a state from a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the two letter state abbreviation
    """
    full_address = full_address.strip()
    last_comma_index = full_address.rindex(",")
    last_space_index = full_address.rindex(" ")
    state = full_address[last_comma_index + 1 : last_space_index]
    state = state.strip()
    return state
 
 
def extract_zipcode(full_address):
    """Extract and return the ZIP code from
    a properly formatted U.S. mailing address.
    Parameter
        full_address: a U.S. mailing address in this format:
            number and street, city, state zipcode
    Return: the ZIP code
    """
    full_address = full_address.strip()
    last_space_index = full_address.rindex(" ")
    zipcode = full_address[last_space_index + 1 : ]
    return zipcode
 
pytest.main(["-v", "--tb=line", "-rN", __file__])