RAIN = "Rain"
n = int(input()) 
rains = []
for _ in range(n):
    date, day, weather = input().split()
    if weather == RAIN:
        rains.append([ list(map(str, date.split('-'))), str(day), str(weather) ])

rains.sort(key=lambda x:int("".join(x[0])))

date, day, weather = rains[0]

print("-".join(date), day, weather)