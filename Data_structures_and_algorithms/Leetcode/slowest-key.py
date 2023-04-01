releaseTimes = [1, 2]
keysPressed = "ba"

d = {}
for i in range(1, len(releaseTimes)):
    d[releaseTimes[i] - releaseTimes[i-1]] = keysPressed[i]

d[releaseTimes[0]] = keysPressed[0]

max_time = max(d.keys())
max_key = d[max_time]

print(max_key)