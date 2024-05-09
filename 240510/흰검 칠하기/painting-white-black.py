OFFSET = 1000 * 100

cur = 0 
arr = [""] * (OFFSET * 2 + 1)

for _ in range(int(input())):

	val, dirc  = input().split()
	val = int(val)

	if dirc == "R":
		for idx in range(val):
			arr[cur + idx + OFFSET] += "B"
		cur += val - 1

	elif dirc == "L":
		for idx in range(val):
			arr[cur - idx + OFFSET] += "W"
		cur -= val - 1


bb, ww, gg = 0 , 0 , 0 
for el in filter(lambda el: el !="" ,arr):
	if (
		len(el) >= 4 
		and el.count("B") >= 2 
		and el.count("W") >= 2
	): 
		gg += 1
	else:
		if el.endswith("B"):
			bb += 1
		else: 
			ww += 1
print(ww, bb, gg )