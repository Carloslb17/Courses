




def many_simple_types(
    num: int,
    decimal: float,
    boolean: bool,
    string: str,
    binary: bytes,
    obj: object,
) -> None :
    
    pass



from typing import Any, List, Tuple, Dict, Set

nums: List[int] = []
vector_xy: Tuple[int] = (1,2)
vector_xy: Dict[str, int] = {
    'Charly': 1,
    'Bob': 2,
}

fruits: Set[str] = {"apple", "kiwi"}


class Animal: