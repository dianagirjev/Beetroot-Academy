def count_lines(name: str) -> int:
    with open(name, "r") as f:
        text = f.readlines()
    return len(text)

def count_chars(name: str) -> int:
    with open(name, 'r') as f:
        nr_chars = len(f.read())
    return nr_chars

def test(name: str) -> None:
    print(count_lines(name))
    print(count_chars(name))