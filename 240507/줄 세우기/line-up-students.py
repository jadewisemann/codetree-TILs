class Student:

    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx + 1
        
    
    def __repr__(self):
        return f"{self.height} {self.weight} {self.idx}"
    
for student in sorted(
    [Student(*input().split(), idx) for idx in range(int(input()))],
    key= lambda x: (x.height, x.weight, x.idx),
    reverse = True
): print(student)