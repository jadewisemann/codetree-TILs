from dataclasses import dataclass

@dataclass
class T:
    name: str
    height: str
    weight: str
    
    def __repr__(self):
        return f"{self.name} {self.height} {self.weight}"        

for el in sorted(
        [T(*input().split()) for _ in range(int(input()))],
        key= lambda x: int(x.height)
    ):
    print(el)