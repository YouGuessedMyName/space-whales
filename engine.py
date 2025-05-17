import copy
from time import sleep
from typing import Tuple

WAIT_NORMAL = 1.5
WAIT_SHORT = 1
WAIT_TINY = 0.5

error_messages: dict = None

def set_error_messages(messages: dict) -> None:
    global error_messages
    error_messages = messages

def out(*args, **kwargs) -> None:
    print(*args, **kwargs)

def play_scene(scene: list[list[str]], do_inp: bool=True, wait: int = WAIT_NORMAL) -> None:
    for frag in scene:
        for line in frag:
            out(line)
            sleep(wait)
        if do_inp:
            input()

def clear_one_line() -> None:
    out("\033[F\033[K", end='')

def clear_two_lines() -> None:
    out("\033[F\033[K\033[F\033[K", end='')

def inp_int(n: None | int = None) -> int:

    err_msg = error_messages["expected_integer"]
    if n:
        err_msg += error_messages["expected_integer_range"].format(num1="1", num2=n)
    err_msg += "."
    clear = False

    while True:
        try:
            inp = input()
            clear_one_line()
            if clear:
                clear_one_line()
            inp = int(inp)
        except Exception:
            out(err_msg)
            clear = True
            continue
        if n:
            if inp < 1 or inp > n:
                out(err_msg)
                clear = True
                continue
        break
    print("{ ", inp, " }")
    return inp

def choice(options: dict) -> str:
    options = copy.deepcopy(options)
    if "q" in options:
        print(options["q"])
        options.pop("q")

    for i, k in enumerate(options):
        out(f'[{i+1}] ', options[k]["o"])
        sleep(WAIT_TINY)
    ch = inp_int(n=len(options))
    i = ch - 1
    l = list(options.values())
    if "r" in l[i]:
        out(l[i]["r"])
        sleep(WAIT_NORMAL)
    return ch
