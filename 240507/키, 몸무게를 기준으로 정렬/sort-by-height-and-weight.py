class People:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)
    
    def __repr__(self):
        return f"{self.name} {self.height} {self.weight}"


for person in sorted(
    [People(*input().split()) for _ in range(int(input()))],
    key= lambda x: (x.height, -x.weight) 
): print(person)