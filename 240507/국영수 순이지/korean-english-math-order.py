from dataclasses import dataclass

@dataclass
class Student:
    name: str
    korean: str
    english: str
    math: str
    
    def __repr__(self):
        return f"{self.name} {self.korean} {self.english} {self.math}"


for el in sorted(
    [Student(*input().split()) for _ in range(int(input()))],
    key= lambda x: (int(x.korean), int(x.english), int(x.math)),
    reverse= True
):
    print(el)