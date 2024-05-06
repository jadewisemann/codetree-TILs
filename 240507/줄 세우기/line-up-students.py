class Student:

    def __init__(self, height, weight, idx):
        self.height = int(height)
        self.weight = int(weight)
        self.index = idx + 1
        
    
    def __repr__(self):
        return f"{self.height} {self.weight} {self.index}"
    
for student in sorted(
    [Student(*input().split(), idx) for idx in range(int(input()))],
    key= lambda x: (-x.height, -x.weight, x.index),
): print(student)