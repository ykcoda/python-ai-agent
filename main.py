# TypedDict
from typing import TypedDict


class Movie(TypedDict):
    title: str
    year: int
    rating: float


my_movie: Movie = {"title": "Inception", "year": 2025, "rating": 8.8}


def process_movie(mov: Movie) -> None:
    print(f"Title: {mov['title']}")
    print(f"Year: {mov['year']}")
    print(f"Rating: {mov['rating']}")


process_movie(my_movie)


class Employee(TypedDict, total=False):
    name: str
    age: int
    department: str


my_employee: Employee = {"name": "John"}

my_employee.get("age", "N/A")


class Address(TypedDict):
    street: str
    city: str
    zip: str


class User(TypedDict):
    username: str
    email: str
    address: Address


user1: User = {
    "username": "Kwame",
    "email": "kwame@gmail.com",
    "address": {"street": "The Greens", "city": "Sunderland", "zip": "SR5 2HT"},
}


print(user1["address"])
