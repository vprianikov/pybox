"""Simple public greeting helpers."""


def hello(name: str = "world") -> str:
    """Build and return a greeting message.

    Args:
        name: Name to include in the greeting. Defaults to ``"world"``.

    Returns:
        A formatted greeting string in the form ``"Hello, <name>!"``.
    """
    return f"Hello, {name}!"
