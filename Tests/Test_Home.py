from streamlit.testing.v1 import AppTest
from pathlib import Path

PATH_APP = Path(__file__).parent.parent / "Home" / "app.py"

def test_app_initial_streamlit():
    """Testing if streamlit app is working properly"""

    # -- Take the path app in string
    at = AppTest.from_file(str(PATH_APP))
    at.run()

    assert not at.exception

def test_initial_elements():
    """Testing if initial elements are working properly"""
    at = AppTest.from_file(str(PATH_APP))
    at.run()

    assert at.title[0].value == "Chi Square Graph"