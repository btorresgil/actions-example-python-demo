from actions_example_python import __version__, main


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_inc() -> None:
    assert main.inc(5) == 6
