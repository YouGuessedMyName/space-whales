def out(s: str):
    print(s)

def inp_int() -> int:
    try:
        return(int(input()))
    except Exception:
        print("Expected an integer.")


def choice(options: list[str]) -> int:
    for i, option in enumerate(options):
        print(f"{i}) {option}")
    return inp_int()
