class Point:

    def __init__(self, x_coor, y_coor, idx):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.idx = idx + 1
        self.distance = int(x_coor)**2 + int(y_coor)**2 



for point in sorted(
    [Point(*map(int, input().split()), idx) for idx in range(int(input()))],
    key= lambda x: (x.distance, x.idx) 
): print(point.idx)