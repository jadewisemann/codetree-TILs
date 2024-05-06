class Number:

    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.sorted_order = 0    

_ = input()

nums = sorted(
    [Number(val, idx) for idx, val in enumerate(map(int, input().split()))],
    key= lambda x: (x.val, x.idx))

for idx, num in enumerate(nums, start=1):
    num.sorted_order = idx

for el in sorted(nums, key=lambda x: x.idx):
    print(el.sorted_order, end=" ")