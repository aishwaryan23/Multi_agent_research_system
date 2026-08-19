import os

from dotenv import load_dotenv

load_dotenv()


def get_secret(name: str) -> str | None:
    """Read a setting from the environment, then Streamlit secrets."""
    value = os.getenv(name)
    if value:
        return value

    try:
        import streamlit as st

        return st.secrets.get(name)
    except (FileNotFoundError, KeyError, AttributeError):
        return None