class Sol:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point =  meeting_point
        self.time = time
    
    def __repr__(self):
        return (
            f"secret code : {self.secret_code}\nmeeting point : {self.meeting_point}\ntime : {self.time}"
        )

i = input().split()
sol = Sol(i[0], i[1], int(i[2]))

print(sol.__repr__())