# Build an RPG character

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    NAME=name
    STR=strength
    INT=intelligence
    CHA=charisma

    if not isinstance(NAME, str):
        return "The character name should be a string"

    if len(NAME) > 10:
        return "The character name is too long"

    if " " in NAME:
        return "The character name should not contain spaces"

    if not isinstance(STR, int) or not isinstance(INT, int) or not isinstance(CHA, int):
        return "All stats should be integers"

    if STR < 1 or INT < 1 or CHA < 1:
        return "All stats should be no less than 1"

    if STR > 4 or INT > 4 or CHA > 4:
        return "All stats should be no more than 4"

    if STR + INT + CHA != 7:
        return "The character should start with 7 points"

    return f"""{NAME}
STR {full_dot*STR}{empty_dot*(10-STR)}
INT {full_dot*INT}{empty_dot*(10-INT)}
CHA {full_dot*CHA}{empty_dot*(10-CHA)}"""

character = create_character("ren", 4, 2, 1)
print(character)
