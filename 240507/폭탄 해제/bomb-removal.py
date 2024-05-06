class Bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

    def __repr__(self):
        return(
            f"code : {self.code}\ncolor : {self.color}\nsecond : {self.time}"
        )
    
print(bomb:=Bomb(*input().split()))