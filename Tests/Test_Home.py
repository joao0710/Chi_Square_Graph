from streamlit.testing.v1 import AppTest
from pathlib import Path


def test_app_inicial_streamlit():
    """Testing if streamlit app is working properly"""
    # 1. Get atual directory
    directory_atual = Path(__file__).parent

    # 2. Return to root and enter in Home directory
    path_app = directory_atual.parent / "Home" / "app.py"

    # 3. Take the path app in string
    at = AppTest.from_file(str(path_app))
    at.run()

    assert not at.exception
