from engine import *
import yaml

def load_dialogue(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        dialogue = yaml.safe_load(file)
    return dialogue

DIALOGUE_PATH = "dutch.yaml"
D = load_dialogue(DIALOGUE_PATH)
set_error_messages(D["errors"])

def what_to_do():
    while True:
        ch = choice(D["beginning"]["what_to_do"])
        if ch == 1:
            choice(D["beginning"]["look_fingers"])
        elif ch == 2:
            choice(D["beginning"]["wake_up"])
        else:
            return

def main():
    play_scene(D["beginning"]["initial"])
    what_to_do()
    play_scene(D["end"]["end"])

if __name__  == "__main__":
    main()