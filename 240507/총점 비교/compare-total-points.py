from dataclasses import dataclass

@dataclass
class Student:
    name: str
    a_score: str
    b_score: str 
    c_score: str

    def __post_init__(self):
        self.score_sum = int(self.a_score) + int(self.b_score) + int(self.c_score)

    def __repr__(self):
        return f"{self.name} {self.a_score} {self.b_score} {self.c_score}"

for el in sorted(
    [Student(*input().split()) for _ in range(int(input()))],
    key= lambda x: x.score_sum
): print(el)