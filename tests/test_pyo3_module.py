from maruta.maruta import sum_as_string, greet


def test_maruta_module():
    """Test maruta module."""
    assert sum_as_string(1, 2) == "3", "sum_as_string(1, 2) should return '3'"
    assert sum_as_string(10, 20) == "30", "sum_as_string(10, 20) should return '30'"
    assert greet() == "Hello, World!", "greet() should return 'Hello, World!'"
    assert (
        greet("maroo") == "Hello, maroo!"
    ), "greet('maroo') should return 'Hello, maroo!'"
