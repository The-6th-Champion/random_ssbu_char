import typing
from rdoclient import RandomOrgClient
from fighters import fighters

def get_random(num: int, r: RandomOrgClient) -> list[int]:
    integers = r.generate_integers(num, 1, 86)
    return integers

def get_fighter(numlist) -> str:
    for i in numlist:
        yield f"{i} - {fighters[i]}"