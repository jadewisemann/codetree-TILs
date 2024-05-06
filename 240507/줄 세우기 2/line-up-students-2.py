class Student:

    def __init__(self, height, weight, index):
        self.height = height
        self.weight = weight
        self.index = index
    
    def __repr__(self):
        return f"{self.height} {self.weight} {self.index}"

for stu in sorted(
    [Student(*map(int, input().split()), idx+1) for idx in range(int(input()))],
    key= lambda x: (x.height, -x.weight)
): 
    print(stu)