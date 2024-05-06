class Agent():
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = int(score)
    
    def __repr__(self):
        return (
            f"{self.code_name} {self.score}"
        )

agents = [Agent(*input().split()) for _ in range(5)]

print(sorted(agents, key= lambda x: x.score)[0])