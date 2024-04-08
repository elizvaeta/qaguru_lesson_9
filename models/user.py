from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    female = 'Female'
    male = 'Male'
    other = 'Other'


class Subject(Enum):
    maths = 'Maths'
    computer_science = 'Computer Science'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    gender: Gender
    user_number: str
    birth_year: str
    birth_month: str
    birth_day: str
    subject: Subject
    hobby: Hobby
    picture: str
    address: str
    state: str
    city: str


liza = User(
    first_name='Elizaveta',
    last_name='Kazova',
    user_email='test@test.com',
    gender=Gender.female,
    user_number='9997776655',
    birth_year='1999',
    birth_month='September',
    birth_day='07',
    subject=Subject.maths,
    hobby=Hobby.music,
    picture='test.jpg',
    address='Russia',
    state='Haryana',
    city='Karnal',
)
