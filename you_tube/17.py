#233
bus_high = 437

n = int(input().strip())
heights = []
while len(heights) < n:
    heights.extend(map(int, input().split()))

for i, h in enumerate(heights, start=1):
    if h <= bus_high:
        print("Crash",i)
        break
else:
    print("No crash")
