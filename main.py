from maruta.maruta import sum_as_string, greet


def main():
    print(sum_as_string(1, 2))  # 3
    assert sum_as_string(1, 2) == "3", "Test case 1 failed"
    assert sum_as_string(10, 20) == "30", "Test case 2 failed"
    print(greet())
    assert greet() == "Hello, World!", "Test case 3 failed"
    print(greet("maroo"))
    assert greet("maroo") == "Hello, maroo!", "Test case 4 failed"


if __name__ == "__main__":
    main()
