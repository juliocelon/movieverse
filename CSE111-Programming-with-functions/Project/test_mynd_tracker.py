"""
Author: Julio Celón
Title: W07 Final Project
"""

from mynd_tracker import read_file, save_file
from os import path
from tempfile import mktemp
import pytest

def test_read_file(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_content = "This is a test file."
    test_file.write_text(test_content)
    result = read_file(str(test_file))

    assert test_file.exists()
    assert test_file.stat().st_size > 0
    assert result == test_content

def test_save_file(tmp_path):
    file_content = "This is a test file."
    test_file = tmp_path / "test_file.txt"
    
    result = save_file(file_content, str(test_file))
    
    assert result == f"File saved successfully: {str(test_file)}"
    
    with open(test_file, 'r') as file:
        content = file.read()
    assert content == file_content

def test_save_file_error(tmp_path):
    file_content = "This is a test file."
    invalid_file_path = str(tmp_path)  

    result = save_file(file_content, invalid_file_path)
    
    assert result.startswith("Error saving file:")

pytest.main(["-v", "--tb=line", "-rN", __file__])