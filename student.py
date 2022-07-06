

class Student:
    def __init__(self, name:str, surname:str, group: str, year_of_birth:int , rating:int):
        self.name = name
        self.surname = surname
        self.group = group
        self.year_of_birth = year_of_birth
        self.rating = rating

    def __str__(self):
        return f'{self.name} {self.surname}, {self.group} , year of birth:{self.year_of_birth}, rating:{self.rating}'



