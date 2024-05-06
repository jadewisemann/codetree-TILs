RAIN = "Rain"

class Forcast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather 

        self.date_int = int("".join(date.split("-")))

    def __repr__(self):
        return f"{self.date} {self.day} {self.weather}"
         
print(sorted(
    filter(
        lambda x:x.weather == RAIN, 
        [Forcast(*input().split()) for _ in range(int(input()))]
    ), key=lambda x:x.date_int)[0])