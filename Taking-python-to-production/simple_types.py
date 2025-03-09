




def many_simple_types(
    num: int,
    decimal: float,
    boolean: bool,
    string: str,
    binary: bytes,
    obj: object,
) -> None :
    
    pass



from typing import Any, List, Tuple, Dict, Set, Union, Type, Optional, TypedDict, NamedTuple

nums: List[int] = []
vector_xy: Tuple[int] = (1,2)
vector_xy: Dict[str, int] = {
    'Charly': 1,
    'Bob': 2,
}

fruits: Set[str] = {"apple", "kiwi"}


class Animal:
    pass


misc_values: List[Union[int, float, str, Type]] = [1, 1.0, "hi", object]

# Using optional for None situations. 
x: Union[int, None] = None
x: Optional[int] = None
# Modern sintax:
x: str | None = None


# - Nested types

student: Dict[str, Union[str, int]] = {
                "Bob": 1, 
}

## Class for anotated Dictionaries.

class Student(TypedDict):
    name: str
    age: int 

## Improves readibility and enforces a way to structure predefined diciotnaries. 
student: Student = {
                "name": "Bob", 
                "age":1,
}

## Also can be used to create dictionaries, and adds autocompletition for dicts
Student(name="Bob", age="4")

## Complex types.

from collections import namedtuple


point_2d = (1, 2)

Point = namedtuple("Point", ["x", "y"])
point_2d = Point(1, 2)
point_2d.x
point_2d.y

class Point(NamedTuple):
    x: int
    y: int
    
    
point_2d = Point(1, 2)
point_2d.x
point_2d.y

## Recursive types.
###


class Student(TypedDict):
    name: str
    age: int 
    friends: List["Student"] # Double quoting the class we get the autocompletition. 
    
    
student: Student = {
                "name": "Bob", 
                "age":1,
                "friends": {
                    "name": "Bob", 
                    "age":1,
                    "friends":[]                    
                    
                }
                    
}

### In modern versions of Python "" don't need to be included. 
from __future__ import annotations

class Student(TypedDict):
    name: str
    age: int 
    friends: List[Student] 
    

